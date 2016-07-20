global config

config = {
        #-------------------Connection Information----------------------
        'HOST':'irc.twitch.tv',
        'PORT':6667,
        'NICK':'py_bot',
        'PASS':'', #Oauth password here.
        'CHAN':'#channel_name',

        'socket_buffer_size':1024, #Amount of bytes allowed through the socket

        'debug':True, #Set to True to enable printing of additional information

        'log':True, #Set to True to log chat entries to file
	'log_dir':'',
}
