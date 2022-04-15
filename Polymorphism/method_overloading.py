#Method Overloading
class student:
    def __init__(self,m1, m2):
        self.m1=m1
        self.m2=m2

    def sum(self,a,b,c):
        s=a+b+c
        return s

    def summ(self,a=None,b=None,c=None):        #here, even if we dont fill all the arguments, it'll accept the
                                                #values and add them acc to the condition.
        if a!=None and b!=None and c!=None:
            s = a + b + c
        elif a!=None and b!=None:
            s=a+b
        elif a!=None:
            s=a

        return s

s1=student(5,2)
print(s1.sum(4,3,12))
print(s1.summ(2,6))
print(s1.summ(2))



