#OOP(Object Oriented Programming) has got 2 properties:-
#1.Attributes--->Variables      2.Behaviour--->Methods(Functions in normall terms but in class we call method)

class Computer:
    def config(self):            #self refers to the argument name for which we need the function to work.
        print("HI","PRO")

x=9
print(type(x))          #inbuilt class

a='9'
print (type(a))         #inbuilt class

b=Computer()
print(type(b))          #class we created

Computer.config(b)      #Here, we want the method(function) to work for argument b; & syntax-->(class.method(self))


