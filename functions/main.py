def add(x,y):
    a=x+y
    return a

result=add(5,2)
print(result)

def add_sub(x,y):
    a=x+y
    b=x-y
    return a,b      #yes, you can return both on the same line.

print("The addition and subtraction of both the number are: ")
result,r2=add_sub(5,2)
print(result,r2)
