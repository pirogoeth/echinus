#!/usr/bin/env python

import eventlet
from eventlet.green import socket, ssl

class Socket(socket.socket):
    """ represents a socket connection. this class is meant to be
        utilised by the Socket4 and Socket6 classes, not by itself,
        though it could be used by itself. """
    
    def __init__(self, addr = None, port = None, use_ssl = False, family = socket.AF_INET):
        """ initialise the socket. """
        socket.socket.__init__(self, socket.AF_INET, socket.SOCK_STREAM)
        
        self.addr = addr
        self.port = port
        self.ssl = use_ssl
        self.family = family
        self.bound = False
        self.closed = False
        
    def __repr__(self):
        """ represent """
        if not self.bound and not self.closed:
            return "<echinus.Socket>"
        elif self.bound and not self.closed:
            return "<echinus.Socket(%s:%s[%s])>" % (self.addr, self.port, self.family)
        elif not self.bound and self.closed:
            return "<echinus.Socket[closed]>"
        
    def filter(self):
        """ this will create a filter on the socket (eg., ssl) """
        
        if ssl is True:
            self.connection = ssl.wrap_socket(self.socket)
        elif ssl is False:
            self.connection = self.socket
        else:
            self.connection = self.socket
    
    def bind(self):
        """ this will bind the socket to +bind+:+port+ and decide if we use ssl or not """
        
        self.filter()
        self.connection.setblocking(0)
        self.connection.bind((self.addr, self.port))
        self.connection.listen(10)
        self.bound = True
    
    def write(self, data, ln = '\r\n'):
        """ writes data to the socket """
        
        data = data if not ln else data + ln
        self.send(data)
    
    def read(self, bs = 1024):
        """ reads +bs+ bytes from the socket """
        
        return self.recv(bs)
    
    def _close(self):
        """ closes the underlying connection """
        
        self.closed = True
        self.bound = False
        self.close()

class ClientSocket(Socket):
    """ represents a server->client socket """
    
    def __init__(self, sock):
        self.addr = sock.getpeername()[0]
        self.port = sock.getpeername()[1]
        self.family = sock.family
        self.connection = sock
    
    def __repr__(self):
        """ represent """
        
        return "<echinus.ClientSocket(%s:%s[%s])>" % (self.addr, self.port, self.family)
    
    def bind(self):
        """ this is a client socket and is unneeded. """
        
        pass
    
    def filter(self):
        """ this is a client socket and is unneeded. """
        
        pass