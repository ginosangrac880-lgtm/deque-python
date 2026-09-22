from abc import ABC, abstractmethod


class DequeInterface(ABC):

    @abstractmethod
    def accessByIndex(self, index):
        pass

    @abstractmethod
    def addToTail(self, num):
        pass

    @abstractmethod
    def addToHead(self, num):
        pass