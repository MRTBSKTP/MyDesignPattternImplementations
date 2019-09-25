# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:52:06 2019

@author: Mert

"""
# Classes that decribe listener and subject objects 
# Observer Pattern:
# "Subject" notifies "Listeners" when its state changes  

from abc import ABC, abstractmethod
# abc is a utility library that enables Abstract Base Classes in Python

class Observable (ABC):
    """ Standartd observable interface """
    
    @abstractmethod
    def registerListener(self):
        pass
    
    @abstractmethod
    def removeListener(self):
        pass
    
    @abstractmethod
    def notifiyListeners(self):
        pass
            
    @abstractmethod
    def checkChange(self):
        pass

    
class Observer (ABC):
    """ Standart observer interface """
    
    @abstractmethod
    def notifyMaster(self):
        pass

# Observable and Observer classes are made abstract so that they can
# act as interfaces...


class Subject (Observable):
    """ Subject that implements observable interface
    will notify observers """
    
    def __init__(self):
        """ encapsulated data field to regulate access """
        self.listenerList = list()
        self.__data = ""
    
    # implement abstract method
    def registerListener(self, *listenerObjects):
        for listener in listenerObjects:
            self.listenerList.append(listener)
    
    # implement abstract method
    def removeListener(self, listenerObject):
        self.listenerList.remove(listenerObject)
    
    # implement abstract method
    def notifiyListeners(self):
        """ send observed data to registered listeners
        data field """
        for listener in self.listenerList:
            listener.data = self.__data
            listener.__call__()
        return 1
    
    # implement abstract method
    def checkChange(self, new_data):
        """ compare new data and existing data to
        an extend to detect changes """
        # A NEW IMPLEMENTATION WILL BE NEEDED
        if new_data == self.__data:
            pass
        else:
            self.__data = new_data
            self.notifiyListeners()
            
    # encapsulation getter/setter methods...
    def setData(self, stream):
        """ method for filling data field """
        new_data = stream
        self.checkChange(new_data)
        return 1
    
    def getData(self):
        return self.__data
    
    def getListenerList(self):
        return self.listenerList
    
    def __str__(self):
        return "Object being listened..."
    
class Listener (Observer):
    """ Objects will feed their data to an upper 
    stream when notified by a Subject object"""
    
    def __init__ (self):
        self.__data = ""
        
    # implement abstract method
    def notifyMaster(self):
        return(self.__data)
    
    def __str__(self):
        return "Listener object..."

    def __call__ (self):
        """ When objects called while holding a payload
        automatically wokes notifyMaster() method to upstream
        information """
        if self.__data:
            self.notifyMaster()
        
            