# Abstract Class & Abstract Method.
# When a method doesnt have the definition but has been declared then its called abstract method.
# Class of abstract methods are called abstract class.
# Condition:- We cannot use create object of abstract class.
# Python doesnt have abstract rule in it by default. So we'll import it.

from abc import *
class Car(ABC):
    @abstractmethod
    def brand(self):
        pass

    def price(self):
        pass

class Lambo(Car):
    def brand(self):
        return "Lambo"

    def price(self):
        return 10

myCar = Lambo()
print(myCar.brand())
print(myCar.price())