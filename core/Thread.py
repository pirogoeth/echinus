#!/usr/bin/env python

import eventlet, traceback
from eventlet.green import thread

class Thread(object):
    """ reimplementation of basic threading capabilities, optimised
        for use by echinus's core """
    
    def __init__(self, function, *args, **kw):
        self.function = function
        self.f_args = args if args is not None else ()
        self.f_kw = kw if kw is not None else {}
        self.status = 'dead'
        
    def __repr__(self):
        """ represent """
        
        return "<echinus.Thread(%s[%s])>" % (self.function, self.status)
    
    def run(self):
        """ runs the thread """
        
        try:
            self.status = 'alive'
            self.thread = thread.start_new_thread(self.function, args = self.f_args, kwargs = self.f_kw)
        except:
            traceback.print_exc(10)

class ListenerThread(Thread):
    """ optimised for listener use """
    
    def __repr__(self):
        """ represent """
        
        return "<echinus.ListenerThread(%s[%s])>" % (self.function, self.status)
    
    def run(self):
        """ starts the listener thread """
        
        try:
            self.status = 'alive'
            self.thread = thread.start_new_thread(self.function.listen, ())
        except:
            traceback.print_exc(10)
    
    def getListener(self):
        """ returns the listener instance managed by this thread """
        
        return self.function
    
    def destroyListener(self):
        """ destroys the listener managed by this thread """
        
        self.function.cancel()
        del self.function