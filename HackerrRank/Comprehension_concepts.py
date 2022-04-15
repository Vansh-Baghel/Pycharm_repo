""" To write 'for' stmts in one line, we use list comprehension.
"""
print("EG:- 1. List comprehensions")
a=[ i for i in range(100) if i%3==0]
print(a)

print()
print("EG:- 2. Dictionary comprehensions")
dict1 = {i:f"item {i}" for i in range(1, 41) if i%10==0}
''' dict always in curly braces. in f string curly braces takes variable and return the value. Here,
 Keys:Values --> 10: 'Item 30' '''


print(dict1)


dict1= {i:f"Item {i}" for i in range (5)}               # You cannot use sq braces or parenthesis.
dict2 = {value:key for key,value in dict1.items()}
print(dict1,"\n", dict2)

print ()

print("EG:- 3. Set comprehensions")
dresses = [dress for dress in ["dress1", "dress2","dress1",
                               "dress2","dress1", "dress2"]]
print(type(dresses))

print ()

print("EG:- 4. Generator comprehensions")
evens = (i for i in range(10) if i%2==0)    # We use parenthesis () for using generators.
print(evens.__next__(),end=" ")             # next is used for generating next iterations. Or could run a for loop.

for item in evens:
    print(item,end=" ")