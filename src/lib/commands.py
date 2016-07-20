import os, requests, json, re, sys, random
from src.config.config import *
import src.lib.irc as irc_
import src.lib.custom_commands as custom_commands
dir = os.path.realpath('src/lib/')
raffle_status = False
raffle_users = []

class commands:

	def __init__(self, config):
		self.config = config
		self.irc = irc_.irc(config)

        #Usage - !hi
	def hi(self):
		return 'Hello!'

	def quit(self, args): #Allows broadcaster to stop bot remotely
		USERSTATE = args[len(args) - 2]
		if re.search('@badges=\w*,?broadcaster,?\w*/[0-9]+', self.irc.parse_userstate(USERSTATE)[0]):
			sys.exit()

        #Usage - !add_command <command_name> "text"
	def add_command(self, args):
		irc = self.irc
		#Set arguments in list to their associated variables
		command_name = args[0]
		username = args[len(args) - 1] #Username and UserState are always appended to the end of the list
		USERSTATE = args[len(args) - 2] #In the order of userstate first, and username second
		del args[0] #Removes command name from args list
		del args[len(args) - 2] #Remove userstate from args
		del args[len(args) - 1] #Removes username from args list
		text = ' '.join(args) #Concatenates args in list to one variable

		#Check if user is mod and command does not already exist
		if 'mod=1' in irc.parse_userstate(USERSTATE) and not command_name in custom_commands.custom_commands:
			try: #Attempt to write to file custom_commands.py
				with open(dir + '/custom_commands.py', 'r') as file: #Get current lines in file
					data = file.readlines()

				#Replace the last line with the new command, and re-add the trailing }
				data[len(data) - 1] = '\t\'' + command_name + '\':' + text.strip('\r') + ',\n}'

				with open(dir + '/custom_commands.py', 'w') as file: #Write changes
					file.writelines(data)

				with open(dir + '/command_cooldowns.py', 'r') as file:
					cd_data = file.readlines()

				#Add command and it's cooldown to the list of commands in command_cooldowns.py
				cd_data[len(cd_data) - 1] = '\t\'' + command_name + '\':{ \'cd\':config[\'default_cmd_cd\'], \'last_used\':0, },\n}'

				with open(dir + '/command_cooldowns.py', 'w') as file:
					file.writelines(cd_data)

				return 'Command !' + command_name + ' added.'
			except:
				print('Error writing to file. Could not add command ' + command_name)

		else:
			print('Command \"' + command_name + '\" already exists, or user \"' + username + '\" not in moderators.')

	def update_command(self, args):
		irc = self.irc
		#Set arguments in list to their associated variables
		command_name = args[0]
		username = args[len(args) - 1] #Username and UserState are always appended to the end of the list
		USERSTATE = args[len(args) - 2] #In the order of userstate first, and username second
		del args[0] #Removes command name from args list
		del args[len(args) - 2] #Remove userstate from args
		del args[len(args) - 1] #Removes username from args list
		text = ' '.join(args) #Concatenates args in list to one variable

		#Check if user is mod and command exists
		if 'mod=1' in irc.parse_userstate(USERSTATE) and command_name in custom_commands.custom_commands:
			try: #Attempt to write to file custom_commands.py
				with open(dir + '/custom_commands.py', 'r') as file:
					data = file.readlines()

				#Replace the last line with the new command, and re-add the trailing }
				data[len(data) - 1] = '\t\'' + command_name + '\':' + text.strip('\r') + ',\n}'

				with open(dir + '/custom_commands.py', 'w') as file:
					for line in data:
						#Don't write previous instance of command to the file.
						if not re.findall('\'' + command_name + '\'(?=:)', line) or re.search('\n}', line):
							file.write(line)

				return 'Command !' + command_name + ' updated.'

			except:
				print('Error writing to file. Could not add command ' + command_name)
		else:
			print('Command \"' + command_name + '\" does not exist, or user \"' + username + '\" not in moderators.')

	#Usage - !remove_command <command_name>
	def remove_command(self, args):
		irc = self.irc
		#Get command_name and username from args list
		command_name = args[0].rstrip()
		username = args[len(args) - 1]
		USERSTATE = args[len(args) - 2]

		if 'mod=1' in irc.parse_userstate(USERSTATE) and command_name in custom_commands.custom_commands:
			try:
				with open(dir + '/custom_commands.py', 'r') as file: #Get file's lines
					data = file.readlines()

				with open(dir + '/custom_commands.py', 'w') as file:
					for line in data: #Loop over file, if command_name is found, do not write that line back to file
						if not re.findall('\'' + command_name + '\'(?=:)', line):
							file.write(line)

				with open(dir + '/command_cooldowns.py', 'r') as file:
					cd_data = file.readlines()

				with open(dir + '/command_cooldowns.py', 'w') as file:
					for line in cd_data:
						if not re.findall('\'' + command_name + '\'(?=:)', line):
							file.write(line)

				return 'Command !' + command_name + ' removed.'

			except:
				print("Error writing to file. Could not remove command " + command_name)

		else:
			print('Command \"' + command_name + '\" does not exist, or user \"' + username + '\" not in moderators.')

	#Usage - !raffle_start
	def raffle_start(self, args):
		irc = self.irc
		global raffle_users
		global raffle_status

		USERSTATE = args[len(args) - 2]

		#Checks if user is the broadcaster and raffle has not already started
		if re.search('@badges=\w*,?broadcaster,?\w*/[0-9]+', irc.parse_userstate(USERSTATE)[0]) and not raffle_status:
			raffle_status = True #Start raffle and notify chat how to enter.
			return 'Raffle started! Type \"!raffle\" to enter.'

	#Usage - !raffle
	def raffle(self, args):
		global raffle_status
		global raffle_users

		username = args[len(args) - 1]
		USERSTATE = args[len(args) - 2]

		#If raffle is on-going and the user has not already entered, append them to the list
		if raffle_status and not username in raffle_users:
			raffle_users.append(username)

	#Usage - !raffle_end
	def raffle_end(self, args):
		irc = self.irc
		global raffle_status
		global raffle_users
		winner = ''

		USERSTATE = args[len(args) - 2]

		#If user is broadcaster and raffle is on-going, select winner and end raffle
		if re.search('@badges=\w*,?broadcaster,?\w*/[0-9]+', irc.parse_userstate(USERSTATE)[0]) and raffle_status:
			if not len(raffle_users) == 0: #Checks if no users entered raffle
				index = random.randrange(0, len(raffle_users)) #Select random index between 0 and the last value in list
				winner = raffle_users[index] #Select winner from list with random index
				raffle_status = False #End raffle
				raffle_users[:] = [] #Clear list

				return 'Winner is @' + winner + ' !'
			else:
				raffle_status = False
				print('No users entered raffle...')
