# Generators:- It'll return the values by iterating them using next method.
# Difference between return and yield is that return will terminate the stmt, but yield will pass values 1 by 1.

def topten () :
   yield 1          #whenever yield is used, it means generator is being used.
   yield 2
   yield 3
   yield 4

values = topten ()

print (values.__next__())
print (values.__next__())

for i in values:            #the value of value will strt from 3 as we've alr called it twice.
   print (i)

print()
print("The square of 1 to 10 are: ")
def sqtopten():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq        #this will iterate 1 1 value, which will be traced by i.
        n += 1

val = sqtopten()

for i in val:
    print(i)

