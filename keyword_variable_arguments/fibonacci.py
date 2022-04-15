def fib(x):
    f1=0
    f2=1
    c=0
    print(f1)
    print(f2)
    for i in range(2,x+1):      #range(5) is read as 2,3,4. therefore we added x+1 to make it as 2,3,4,5.
        c=f1+f2
        print(c)
        f1=f2
        f2=c

fib(5)



