#In python, its nothing like pass by reference or value
def update(x):
    print("ID of x before update: ",id(x))          #same values will have same id
    x=10
    print("ID of x after update: ", id(x))          #as value changes, the id changes
    print("Value of x: ", x)


a=8
print("ID of x: ",id(a))
update(a)
print("Value of a: ",a)


