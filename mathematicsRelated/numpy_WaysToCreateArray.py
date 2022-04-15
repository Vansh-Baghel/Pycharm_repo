from numpy import *
#we dont need to give typecode
#Ways to create arrays are:-
#1.array()
a=array([3,1.,5,2,6])
print("The datatype and the array is: ",a.dtype,a)

#2.Linspace(start,end,no.. of parts it will be divided)
b=linspace(0,14,7)
print (b)

#3.Arange(start,end,skipping range)
c=arange(0,14,2)
print(c)
d=arange(0,14,4)
print(d)

#4.Logspace, idk its use
e=logspace(0,100,10)
print (e)

#5.Zeros  & 6. Ones
f=zeros(4)
print(f)
g=ones (4)
print(g)
f=ones(4,int)
print(f)