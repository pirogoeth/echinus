#!/usr/bin/python

import eventlet, Socket, Thread, sys
from Socket import ClientSocket
from Thread import ListenerThread
from eventlet.green import socket

class Listener(object):
    """ represents a socket listener """
    
    def __init__(self, socket):
        self.socket = socket
        self.listening = None
        
    def __repr__(self):
        """ represent """
        
        return "<echinus.Listener(%s)>" % (self.socket.__repr__())
    
    def listen(self):
        """ wrapper for _listen """
        
        self.listening = True
        sys.stdout.write("Now listening on: %s" % (self.socket.gethostbyname()))
        eventlet.spawn(self._listen).wait()
    
    def _listen(self):
        """ backend: listen on +socket+ """
    
        while self.listening is True:
            try:
                # this first line will cause all future failures in this specific block. no more error handling is needed.
                client, address = self.socket.connection.accept()
                client = ClientSocket(client)
                client.write('Connection successful!', '\r\n')
                client.close()
            except (socket.error):
                pass
    
    def cancel(self):
        """ stop listening on this socket and close """
    
        self.listening = False
        self.socket.close()

class Server(object):
    """ represents the core manager of everything. """
    
    def __init__(self, socketlist):
        self.sockets = socketlist
        self.listeners = []
        self.threads = []
        
    def __repr__(self):
        """ represent """
        
        return "<echinus.Server(%s)>" % (len(self.listeners))
    
    def add_socket(self, socket):
        """ adds a new socket to the collection and begins listening """
        
        listener = Listener(socket)
        self.listeners.append(listener)
        listener_t = ListenerThread(listener)
        self.threads.append(listener_t)
        listener_t.run()

    def listen_all(self):
        """ starts an accept loop for all sockets in the list """
        
        self.listening = True
        for socket in self.sockets:
            listener = Listener(socket)
            self.listeners.append(listener)
            listener_t = ListenerThread(listener)
            self.threads.append(listener_t)
            listener_t.run()
