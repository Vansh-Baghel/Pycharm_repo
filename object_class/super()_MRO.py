class A:
    def __init__(self):
        print("A wala init")

    def number1(self):
        print('1')

    def number2(self):
        print('2')

class B(A):                 #A is inherited into B by typing such syntax
                            #all the methods of A can be used while using B class

    def __init__(self):
        super().__init__()       #through super we can call any method from A. Now it'll also print A ka init
        print("B wala init")

    def number3(self):
        print('3')

    def number4(self):
        print('4')

class C(B):             #In this, A and B both are herited into C. #multiple inheritance
    def __init__(self):
        super().__init__()      #this time it'll print init of both the class
        print("C wala init")

    def number5(self):
        print('5')

class D:
    def __init__(self):
        print("D wala init")

class E(A,D):               #NOTE:-u cannot write child classes in brackets, eg (A,B) qould've been wrong.
    def __init__(self):
        super().__init__()          #this time it'll print init of LHS class [A(LHS),D(RHS)]
                                    #this is called method resolution order
        print("E wala init")

print("When class A is called: ",end="")
a=A()

print("When class B is called with super: ",end="")
b=B()

print("When class C is called: ",end="")
c=C()

print("When class D is called: ",end="")
e=E()


