#!/usr/bin/env python

class User(object):
    """ represents an IRC user """
    
    def __init__(self, nick, ident, host, ip):
        # connection
        self.nick = nick
        self.ident = ident
        self.host = host
        self.ip = ip
        # struct
        self.channels = []
        self.metadata = {}
        
        