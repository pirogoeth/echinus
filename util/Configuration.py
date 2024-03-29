#!/usr/bin/env python

class Configuration(object):
    """ this will hold the configuration.
        it will not actually read the configuration itself, but it
        will carry everything """
    
    def __init__(self):
        """ initialise the container 
            store in key:value format withing the certain category """
        self.container = {}
        self.loaded = False
        
    def __repr__(self):
        """ represent """
        return "<Configuration(%s)>" % (len(self.container))

    def __add__(self, set):
        """ addition function to add a set to the container """
        self.container[set[2]].update({set[0]: set[1]})
    
    def __sub__(self, set):
        """ subtraction function to remove a set from a category. """
        self.container[set[0]].__delitem__(set[1])
    
    def __iadd__(self, category):
        """ p/e function to add a category """
        self.container.update({category: {}})
        return self
    
    def __isub__(self, category):
        """ s/e function to remove a category """
        if self.container[category]:
            self.container.__delitem__(category)
        return self
    
    def getCategory(self, category):
        """ return a category """
        return self.container[category] if self.container.__contains__(category) else None
    
    def getValue(self, category, key):
        """ return [category:key] """
        return self.container[category][key] if self.container[category].__contains__(key) else None
    
    def unload(self):
        """ unload an entire configuration """
        self.container.clear()
        self.loaded = False
        
    def load(self, file):
        """ load a file and read in the categories and variables """
        self.file = file
        f = open(file, 'a+')
        if self.loaded: self.container.clear()
        category = None
        for line in f.readlines():
            line = line.strip('\n')
            if line.startswith('#'): 
                continue
            elif line.endswith('{'):
                # category
                category = line.split('{')[0].rstrip()
                self += category
                continue
            elif line.startswith('}') and line.endswith('}'):
                category = None
            elif '=' in line:
                set = line.split('=')
                l = len(set[0])
                if set[0][l-1] == ' ':
                    set[0] = set[0][:l-1].lstrip()
                if set[1][0] == ' ':
                    set[1] = set[1][1:]
                set.append(category)
                self + set
                continue
            continue
        self.loaded = True
        f.close()