from numpy import *
a=([3,1,5,2])
b=([6,3,8,5])
#These operations comes under vectorized operations
print ("Addition of both array gives: ",end="")
print(a+b)

print("Sum of a: ", end="")
print(sum(a))

print("Joining two arrays: ",end="")
print(concatenate([a,b]))

print("Sorting array a: ",end="")
print(sort(a))

print("Can find sin,cos,tan,etc too")
print("Sin of a is: ",end="")
print(sin(a))

print("Maximum value in a is: ",end="")
print(max(a))

#COPYING ARRAYS
a=([3,24,1,5,6])
print(a)
print("Coping new value of a into b: ",end="")
b=a.copy()
print(b)


