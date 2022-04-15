#Operator overloading:- Here method name is same but the type is different
#explore more of such type.

class Student:
    def __init__(self,m1,m2) :
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):           # operator overloading is done by add and as add is inbuilt method, it'll
                                        # work automatically even if we dont call it.
                                        # add has its own way to work but we gave it information to work acc to us
                                        # This is overloading. __add__ --> +
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __str__(self):          # We overloaded the existing method. The output would've been the address of
                                # s1 if we kept it that way.
        return self.m1,self.m2

s1 = Student (58,69)            # 1st m1, 2nd m1
s2 = Student (60, 65)

s3 = s1+s2

print(s3.m1)             # 58+60

a=9
print(a)
print(s1.__str__())       # behind its calling a method called str.



