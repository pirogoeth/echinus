#!/usr/bin/env python

from __init__ import timestamp

class User(object):
    """ represents an IRC user """
    
    def __init__(self, server, (sock, address)):
        """ instantiate a new user object """
        
        self.server = server
        # IP stuff
        self.socket = sock
        self.addr = address
        self.ip = address[0]
        self.port = address[1]
        # user info
        self.nickname = "*"
        self.realname = "unknown"
        self.username = "unknown"
        # metadata
        self.channels = []
        self.metadata = {}
        self.away = False
        self.oper = False
        # hostname
        if server.hostcache.has_key(self.ip):
            self.hostname = server.hostcache[self.ip]
        else:
            try:
                socket.gethostbyaddr(self.ip)[0]
            except:
                self.hostname = self.ip
            self.server.hostcache[self.ip] = self.hostname
        connections = filter(lambda u: u.ip == self.ip, self.server.users)
        if len(connections) > 3:
            self.quit("Too many connections from %s" % (self.ip))