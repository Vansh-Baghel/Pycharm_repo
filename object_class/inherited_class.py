class A:
    def number1(self):
        print('1')

    def number2(self):
        print('2')

class B(A):                 #A is inherited into B by typing such syntax
                            #all the methods of A can be used while using B class
    def number3(self):
        print('3')

    def number4(self):
        print('4')

class C(B):             #In this, A and B both are herited into C. #multiple inheritance
    def number5(self):
        print('5')

a=B()               #a define krne k baad we can use a.number3
a.number3()
