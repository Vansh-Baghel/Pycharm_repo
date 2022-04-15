from array import *

arr=array('i',[])
n=int(input("Enter the number of values you want to enter: "))
print("Enter the values: ",end="")
for i in range(n):
    x=int(input())
    arr.append(x)       #here the values will be added into arr one by one as the loop runs.
print (arr)

print("The reverse of the following array: ", end="")
arr.reverse()
print(arr)

a=int(input("Enter the number whose index you need: "))
k=0                     #used to find the index of that number
for j in arr:
    if (j==a):
        print(k)
        break
    k+=1

