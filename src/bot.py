import src.lib.irc as irc_ #Import irc library
import src.lib.command_functions as commands #Import command_functions library
import importlib

class twitch_bot:

	#instantiation of twitch_bot object
	def __init__(self, config):
		#Creating irc and socket objects
		self.config = config
		self.irc = irc_.irc(config)
		self.socket = self.irc.get_socket()

	def start(self):
		irc = self.irc
		sock = self.socket
		config = self.config

		while True: #Loop to read chat
			data = sock.recv(config['socket_buffer_size']).decode("UTF-8") #Receieve messages from socket

			if len(data) == 0: #If no data is received, re-connect
				print('Connection lost, reconnecting.')
				sock = self.irc.get_socket()

			if config['debug']: #Enable debugging
				print(data)

			irc.check_ping(data) #Check if twitch is sending a ping message to bot

			if irc.check_for_message(data): #Parse messages
				#Separate username, message, and userstate into a dictionary, and then assign each to a variable
				message_list = irc.get_message(data)
				username = message_list['username']
				message = message_list['message']
				USERSTATE = message_list['USERSTATE']

				print(username + ": " + message)

				#Check if message is a command
				if commands.is_valid_command(message) or commands.is_valid_command(message.split(' ')[0]):
					command = message
					args = command.split(' ') #If arguments are provided, separatee them into a list
					command = command.split(' ')[0] #Remove args from command
					del args[0] #Detele command name from args list
					args.append(USERSTATE)
					args.append(username) #Add username to end of args list

					result = commands.run_command(command, args)

					if result: #Send reply to user that ran command
						response = '@{} {}'.format(username, result)
						irc.send_message(response)

				if commands.check_is_custom_command(message):
					result = commands.run_custom_command(message)

					if result:
						response = '@{} {}'.format(username, result)
						irc.send_message(response)
