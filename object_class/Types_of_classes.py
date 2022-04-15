#Types of methods:- 3 types...

#1.Class Method
#2.Instance Method---> A.Accessor method, B. Mutator method
#3.Static Method

class comp:
    school="telusko"                #Class variable.

    def __init__(self,m1,m2):       #Mutator type method
        self.m1=m1
        self.m2=m2

    #def __init__(self,m1,m2):       #Accessor type method
        #self.m1=m1
        #self.m2=m2

    def avg(self):
        return (self.m1+self.m2)/2

    @classmethod                    #decorator to use class method
    def getSchool(cls):             #To make changes in class we dont use self, we use cls
        return cls.school           #This will return the school value ie cllss variable ka value

    @staticmethod                   #decorator to use static method
    def info():                     #In this method, the bracket will be empty.
        print("This is the sky:)")

s1=comp(91,3)
s2=comp(99,40)
print(s1.m1, s1.m2, s2.m1, s2.m2)

print (s1.avg())

print (comp.getSchool())

print(comp.info())