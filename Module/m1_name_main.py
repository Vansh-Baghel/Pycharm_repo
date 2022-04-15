#Module:- We use module to break a big project into number of steps and use them in different files
# by importing

#we will import this file in m2

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    return a/b

print("This file is", __name__)                 #here, if the file is m1 ie main file then the output will have
                                                #main, otherwise if its ran in m1 file then name will be
                                                #replaced by the file name ie m1.

if __name__ == "__main__" :                     #means only if its the main file, then run this code, else
                                                #when imported this file, then just ignore these stmts.
    print("Hello, I am Vansh Baghel :)")
    print("Lets start with our project man!!")





