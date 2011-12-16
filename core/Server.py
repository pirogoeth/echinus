#!/usr/bin/python

import eventlet, Socket, Thread
from Socket import ClientSocket
from Thread import ListenerThread
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