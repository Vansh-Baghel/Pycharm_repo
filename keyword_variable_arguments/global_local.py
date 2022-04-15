a=10                #global
def num():
    a=15            #local
    print("In function: ",a)

num()
print("Outside the function: ",a)

print()

a=10                #global
def nums():
    a
    print("In function: ",a)

nums()
print("Outside the function: ",a)

print()

a=10                #global but will be local due to function usage
def nums():
    global a        #we used global function which will act as global now
    a=200
    print("In function: ",a)

nums()
print("Outside the function: ",a)



