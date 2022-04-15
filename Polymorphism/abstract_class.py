# Abstract Class & Abstract Method.
# When a method doesnt have the definition but has been declared then its called abstract method.
# Class of abstract methods are called abstract class.
# Condition:- We cannot use create object of abstract class.
# Python doesnt have abstract rule in it by default. So we'll import it.

from abc import *
class computer(ABC):
    @abstractmethod         #If ye nhi daalte toh abstract ka object create krna possible hojata.
    def process(self):
        pass

class laptop(computer):
    def process(self):
        print("Its running")

class board():                  #if computer ko inherit krta toh error ata print krte waqt, bcoz abstract h vo.
    def process(self):
        print("Its writing.")

class programmer():
    def work(self,com):
        print("Solving bugs")
        com.process()           #it'll go to process of laptop

#com1=computer()                #These 2 are objects of abstract class.
#com1.process()
com1=laptop()
com1.process()

print()

prog=programmer()
prog.work(com1)
a=board()
a.process()
