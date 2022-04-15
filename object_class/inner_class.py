class student:
    def __init__(self):
        self.name='vansh'
        self.age=16
        self.lap = self.laptop      #inner class object.
                                    #here, we have define the object in the outer class & while using
                                    #in code, we just need to call student.lap as lap is the name we've given.

    def show(self):
        print(self.name,self.age)

    class laptop:
        def __init__(self):
            self.brand="HP"
            self.cpu="i5"
            self.ram=8

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=student()
s2=student()

print(s1.show())
a=student.laptop()      #This step is very v v imp, syntax-->(outerclass.innerclass.object_of_innerclass)
print(a.show())
