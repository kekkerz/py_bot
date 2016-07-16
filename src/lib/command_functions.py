#Import config and commands
from src.config.config import *
#from src.lib.commands import *
import src.lib.commands as commands_
#from src.lib.custom_commands import *
import src.lib.custom_commands as custom_commands
import inspect
import importlib

commands = commands_.commands(config)

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