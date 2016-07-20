from src.config.config import *
global command_cooldowns

#Add cooldowns for commands here. If a command is not listed here, the bot will assume no cooldown
cooldowns = {
	'hi':{
		'cd':config['default_cmd_cd'],
		'last_used':0,
	},

	'add_command':{
		'cd':config['default_cmd_cd'],
		'last_used':0,
	},

	'update_command':{
		'cd':config['default_cmd_cd'],
		'last_used':0,
	},

	'remove_command':{
		'cd':config['default_cmd_cd'],
		'last_used':0,
	},
}