import socket, re, time, sys, requests, json, os #Import required libraries
from src.lib.custom_commands import *

class irc:

	def __init__(self, config):
		self.config = config

	def check_is_command(self, message, valid_commands): #Check if message is command
		for command in valid_commands:
			if command == message:
				return True

	def get_user_list(self): #Get list of users currently logged in to chat
		request = requests.get('https://tmi.twitch.tv/group/user/' + self.config['CHAN'].replace('#', '') + '/chatters')
		data = json.loads(request.text)
		return data

	def parse_userstate(self, USERSTATE): #Separate userstate entries into a list
		states = USERSTATE.split(';')
		return (states)

	def check_for_message(self, data): #Check incoming data for user messages
		if re.search(':\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :', data):
			return True

	def check_ping(self, data): #Check if twitch is sending PING to bot
		if data[:4] == 'PING':
			self.sock.send('PONG tmi.twitch.tv\r\n'.encode())

	def get_message(self, data): #Return username and message from provided data
		return {
			'username':re.findall(':\w+', data)[0].replace(':', ''),
			'message':re.findall('PRIVMSG #[a-zA-Z0-9_]+ :(.+)', data)[0],
			'USERSTATE':data.split()[0]
		}

	def send_message(self, data): #Send messsage to chat as bot
		self.sock.send('PRIVMSG {} :{}\n'.format(self.config['CHAN'], data).encode())

	def log_message(self, username, message): #Log chat messages to file. Default location is sr/logs/'date'.log
		if self.config['log_dir'] == '': #Set directory for logs
			dir = os.path.realpath('src/logs/')
		else:
			dir = os.path.realpath(self.config['log_dir'])

		with open(dir + "/" + time.strftime('%m-%d-%Y') + '.log', 'a+') as file:
			file.write(time.strftime('%H:%M:%S') + ' - ' + username + ': ' + message + '\n')

	def get_socket(self): #Create socket object, login, and join channel configured in config.py
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		self.sock = sock

		try: #Attempts to connect to host and port configured in config.py. Prints error on exception
			sock.connect((self.config['HOST'], self.config['PORT']))
		except:
			print('Cannot connect to server (%s:%s).' % (self.config['HOST'], self.config['PORT']), 'error')

		#Send login and channel information to server
		sock.send('USER {}\r\n'.format(self.config['NICK']).encode())
		sock.send('PASS {}\r\n'.format(self.config['PASS']).encode())
		sock.send('NICK {}\r\n'.format(self.config['NICK']).encode())
		sock.send('CAP REQ :twitch.tv/membership\r\n'.encode())
		sock.send('CAP REQ :twitch.tv/tags\r\n'.encode())
		sock.send('CAP REQ :twitch.tv/commands\r\n'.encode())
		sock.send('JOIN {}\r\n'.format(self.config['CHAN']).encode())

		return sock
