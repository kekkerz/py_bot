#Import config and commands
from src.config.config import *
import src.lib.commands as commands_
import src.lib.custom_commands as custom_commands
import src.lib.command_cooldowns as command_cooldowns
import inspect, time, importlib

commands = commands_.commands(config)

def command_on_cd(command): #Checks cooldown status for command
	command = command.replace('!', '')
	try: #Compare current time with the time command was last used, and it's cooldown time.
		if (time.time() - command_cooldowns.cooldowns[command]['last_used']) < command_cooldowns.cooldowns[command]['cd']:
			return True
	except KeyError: #If command is not listed in the cooldowns dict, assume no cooldown
		return False

def update_cd(command): #Update last used time for command
	command = command.replace('!', '')
	try:
		command_cooldowns.cooldowns[command]['last_used'] = time.time()
	except KeyError:
		pass

def reload_cooldowns(): #Reload cooldowns module after new commands are added. This prevents needing to restart the bot.
	importlib.reload(command_cooldowns)

def check_is_custom_command(command):
        importlib.reload(custom_commands) #Reload custom_command module to ensure any newly added commands are loaded
        command = command.replace('!', '').rstrip().lower()
        if command in custom_commands.custom_commands: #Check if command is listed in custom_commands module
                return True

def is_valid_command(command): #Check if command is valid
        command = command.replace('!', '').rstrip().lower() #Removes !, trailing characters such as \r\n, and converts string to lowercase

        try: #Attempt to set function variable to provided command
                function = getattr(commands, command)
                return True
        except AttributeError: #If command not found in commands.py, return False
                return False

def run_command(command, args): #Execute command
        command = command.replace('!', '').rstrip().lower()

        try:
                function = getattr(commands, command)
        except AttributeError:
                print("Command \"" + command + "\" not found...")

        try: #If arguments are given, and the function takes arguments, pass args to function
                inspect.getargspec(function)[0][1]
                return function(args)
        except IndexError:
                return function()

def run_custom_command(command):
        command = command.replace('!', '').rstrip().lower()

        return custom_commands.custom_commands[command]
