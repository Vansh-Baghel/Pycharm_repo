#decorator:- its used to edit a function without changing the existing function.
def div(a,b):
    print(a/b)

def smart_div(func):      #here func is written to add the function in further steps which we want to change.
    def inner(a,b):
        if a<b:
            a,b=b,a         #if a is smaller than b, then swap hoga
        return func(a,b)
    return inner

div1=smart_div(div)

div1(2,4)                   #if decorator use nhi krte, toh ans 0.5 ata



