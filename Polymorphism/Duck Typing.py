#1. Duck Typing:-Here class of object is less important than the object.We execute class by calling it
#through its object

class PyCharm:
    def execute (self):
        print ("Compiling")
        print ("Running")

class MyEditor:
    def execute (self):
        print ("Spell Check")
        print ("Convention Check")
        print ("Compiling")
        print ("Running")

class Laptop:
    def code (self,ide):
        ide.execute()

ide = PyCharm()
a = Laptop()
a.code(ide)         #We need to pass ide as argument.
print()
ide= MyEditor()
b = Laptop()
b.code(ide)