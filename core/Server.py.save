#!/usr/bin/python

import eventlet, time, Socket
from select import select
from Socket import ClientSocket
from eventlet.green import socket

class Server(Socket):
    """ represents the core manager of everything. """
    
    def __init__(self):
        """ initialise the server and instantiate w/ Socket.Socket().__init__() """
        
        Socket.__init__(self)
        
        self._hostcache = {}
        
        self.clients = []
        self.channels = []

    def __repr__(self):
        """ represent """
        
        return "<echinus.Server(%s)>" % (len(self.listeners))
    
    def run():
        """ run the server. """
        
        while True:
            time.sleep(0.00005)
            # get users posting a message
            sendable = [user for user in self.clients if user.sendbuffer]
            # select operations
            read, write, error = select([self] + self.clients, sendable, self.clients, 25.0)
            # remove users that have errored
            for user in error:
                user.quit("Read error: Connection reset by peer")
            # look for new connections
            [self.clients.append(User(self, self.accept())) for user in read]