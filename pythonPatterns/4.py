#range(0,n) or range(n) are same
for i in range(5):
    c = i+1
    for j in range (i+1):        #if (i+1) nhi daalte toh j=0 hota for i=0 which means 0 times value print hoti

        print(c,end="")
        c-=1

    print()