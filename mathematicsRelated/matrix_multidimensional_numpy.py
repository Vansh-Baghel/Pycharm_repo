from numpy import *
arr1=array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(arr1)
print("The datatype of the array: ",end="")
print(arr1.dtype)
print("The dimension of the array: ",end="")
print(arr1.ndim)
print("The shape of the array: ",end="")
print(arr1.shape)
print("The size of the array: ",end="")
print(arr1.size)

#matrix function
a1=matrix('1 2;3 4;5 6;7 8')        #semi colon is used to separate rows
print(a1)

#adding & multiplying 2 arrays
m1=matrix('1 2; 3 4')
m2=matrix('3 4; 5 6')
m3=m1+m2
m4=m1*m2
print("Addition of 2 matrices is: ")
print(m3)
print("Multiplication of 2 matrices is: ")
print(m4)

