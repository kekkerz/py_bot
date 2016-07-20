global config

config = {
        #-------------------Connection Information----------------------
        'HOST':'irc.twitch.tv',
        'PORT':6667,
        'NICK':'py_bot',
        'PASS':'', #Oauth goes here
        'CHAN':'#channel_name',

        'socket_buffer_size':1024, #Amount of bytes allowed through the socket

        'debug':False, #Set to True to enable printing of additional information

        'log':False, #Set to True to log chat entries to file
	'log_dir':'',

	'sub_only_links':False, #Only subs can paste links in chat
	'link_timeout_message':'Only subs can paste links.', #Message sent to use when they are timed out
	'link_timeout_time':30, #Duration of timeout

	'default_cmd_cd':5,
}
