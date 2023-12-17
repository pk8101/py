#abstract class 
# it contain abstract methods but abstract dont have class we need to call it from Module abc
# and it contain:
#1.ABC class and 2.abstractmethod

from abc import ABC,abstractmethod

class A(ABC): #ABC class inhereted
    def __init__(self) :
        print("its class A")
        
    @abstractmethod
    def hi(self):
        pass
    @abstractmethod
    def hello(self):
        pass


class B(A):
    def __init__(self):    #if this init method is not implemented then class A init will be executed
        print("hello its class B")
    def hi(self):
        pass
    def hello(self):
        pass


s1=B()