def fact(x):
    if x==1:                #from here, the 1st value in x-1 will be entered
        return 1

    return x*fact(x-1)

r=fact(5)
print(r)
