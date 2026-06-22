from abc import ABC, abstractmethod
class AbstractClass(ABC):
    @abstractmethod
    def abcd(self):
        pass
class Main(AbstractClass):
    def cdef(self):
        return "This is also abstract method "
    def abcd(self): 
        return "This is an implemented abstract method"
m=Main()
print(m.cdef())
print(m.abcd())