#Two types of arguments:- 1.Formal arguments 2.Actual argument

#1.Formal arguments have 4 types
#A.Position

def person(name,age):
    print ("1. ",name,age)

a=person("Vansh",18)

print("2. ",end="")
#B. Keyword
b=person(age=16,name="Lucky")


#C.Default
def game(graphics,category="fighting"):     #here the default value is of category
    print("3. ",category,graphics)

c=game("high")

#D.Variable length
def num(a,*b):           #here * will allow more than 1 value to be stored in b.
    c=a
    for i in b:     #here for loop is required bcoz we cant add int & tuple as both are of different datatpyes.
        c+=i        #c=a and i will be every value in b, therefore adding them is like adding a & b
    print("4. ",c)

d=num(5,3,9,6)
