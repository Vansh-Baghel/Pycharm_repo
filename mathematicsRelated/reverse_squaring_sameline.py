from array import *
values=array('i',[5,3,2,6])
print(values)

print("the address and size of int array is:",values.buffer_info())         #address and size will be displayed

values.reverse()                    #reversing array
print("reverse of int array: ",values)

print("printing the numbers in same line: ",end="")     #end used here to print the values on the same line.
for i in values:
    print(i,end=" ")

print()

value=array('u',['r','w','a','g'])
print(value)

value.reverse()
print("reverse of character array :",value)

#printing the old array values into new array
newArr=array(values.typecode, (z for z in values))      #typecode is used when we dont know the datatpe of that
                                                        # is unknown. And values is the name of the variable.

print("The square of int array which was in reverse order: ",end="")
for z in newArr:
    print(z*z ,end=" , ")       #square of values of old array; & u can give space or comma simply by tpying in end

