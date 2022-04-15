def check(n):
    even=0
    odd=0
    for i in n:

        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even , odd

n=[3,6,1,7,42,15,3]

even, odd = check(n)        #written to get the return value stored
print("Even : {} & Odd : {}".format(even,odd))    #format function helps to print the value between the print stmt

