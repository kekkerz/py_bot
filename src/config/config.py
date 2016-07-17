global config

config = {
        #-------------------Connection Information----------------------
        'HOST':'irc.twitch.tv',
        'PORT':6667,
        'NICK':'py_bot',
        'PASS':'oauth:lj9tqbnho79ghubrnm5mc6x1sj1fg6',
        'CHAN':'#abb1995',

        'socket_buffer_size':1024, #Amount of bytes allowed through the socket

        'debug':True, #Set to True to enable printing of additional information

        'log':False #Set to True to log chat entries to file
}
