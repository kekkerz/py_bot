import os, requests, json, re, sys
from src.config.config import *
import src.lib.irc as irc_
import src.lib.custom_commands as custom_commands
dir = os.path.realpath('src/lib/')

class commands:

	def __init__(self, config):
		self.config = config
		self.irc = irc_.irc(config)

        #Usage - !hi
	def hi(self):
		return 'Hello!'

	def quit(self, args): #Allows broadcaster to stop bot remotely
		USERSTATE = args[len(args) - 2]
		if '@badges=broadcaster/1' in self.irc.parse_userstate(USERSTATE):
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

				return 'Command !' + command_name + ' added.'
			except:
				print('Error writing to file. Could not add command ' + command_name)

		else:
			print('Command \"' + command_name + '\"" already exists, or user \"' + username + '\" not in moderators.')

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
				file.close()

				with open(dir + '/custom_commands.py', 'w') as file:
					for line in data: #Loop over file, if command_name is found, do not write that line back to file
						if not re.findall('\'' + command_name + '\'(?=:)', line):
							file.write(line)
				file.close()

				return 'Command !' + command_name + ' removed.'

			except:
				print("Error writing to file. Could not remove command " + command_name)

		else:
			print('Command \"' + command_name + '\" does not exist, or user \"' + username + '\" not in moderators.')
