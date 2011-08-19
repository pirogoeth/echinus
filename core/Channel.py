#!/usr/bin/env python

from util import timestamp

class Channel(object):
    """ represents a channel and its structure. """
    
    def __init__(self, name = None):
        """ create the channel """
        
        self.name = name
        self.time_c = timestamp()
        self.topic = ''
        self.users = []
    
    def __repr__(self):
        """ represent """
        
        return "<echinus.Channel(%s)>" % (self.name)