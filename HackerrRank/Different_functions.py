#1. split() :- Used to separate string into list.
print("EG:-1.")
str_input="Space separation"
str_I1="Separated_by_dash"
print(str_input.split(" "))
print(str_I1.split("_"))            #The value into "" will be the point where values will be splitted.
print()

#2. join() :- Used to join different values of list. List to string conversion. You cannot join w/o converting
              #it into a list bcoz it adds the join by replacing "" k bahar ka part.
print("EG:-2.")
a=["How","Are","You"]
print("_".join(a))
print()

#3. variable.replace(value, newvalue) :- Used to replace the word in variable from new value.
print("EG:-3.")
name="VansssBaghel"
new_name=name.replace("Vansss","Vansh")
print(new_name)
print()

#4. String & f-String:- Used to add values into print stmt.
print("EG:-4.")
add="Vansh"
b="This is {}'s book".format(add)
print(b)
a="my"
b= f"This is {a} book"
c="This is "+a+"book"
print(b)
print(c)

""""
5. list(variable):- Used to convert the value of variable into list.

6. map & list:- Converts the datatype of a variable in one step. Usually used to convert string into int and we
                use list and map tgt bcoz map is a object & list just lists the values.
                Syntax:- list(map(function/module, variable))
"""
print()
print("EG:- 6.")
a=["8", "23", "32", "94"]         #You cannot put character value in a and expect map to change into int.
print(list(map(int,a)))

def squ(a):
    return (a*a)

def cube(a):
    return a*a*a


num = [8, 5, 3, 2]
func=[squ, cube]
for i in num:
    val=list(map(lambda x:x(i),func))   #x ko leke x(i) return hora h.
    print(val)
print()

#7. list(filter()):- filters the value of variable. if the condition is true, it keeps the value, else remove.
                    #This is also object, so we need list.
print("EG:-7.")
def greater(num):
    return num>5

list_num=[1,32,1,4,1,56,7,654,32,1]
a=list(filter(greater,list_num))
print(a)

"""" 8. reduce(function,variable):- It'll make a large list of numbers into a single number.
                                #We need to import functools for using reduce.

 9. (str).isalnum()
 Return true if all characters in the string are alphanumeric (means alphabats and numbers), false otherwise.

 10. (str).isalpha()
 Return true if all characters in the string are alphabetic and there is at least one character,false otherwise.

 11. isdigit()
 Return true if all characters in the string are digits and there is at least one character, false otherwise.

 12. str.istitle()
    Return true if the string is a titlecased string means sab words should strt with uppercase. Return 
    false otherwise.
    

 13. str.isupper()
 Return true if all cased characters 4 in the string are uppercase and there is at least one cased character,
 false otherwise.
 
 14. str.islower()
Return true if all cased characters 4 in the string are lowercase and there is at least one cased character,
 false otherwise.

 15. str.isspace()
 Return true if there are only whitespace characters in the string and there is at least one character,
 false otherwise.
 
 16. max(name)
     min(name)
     
 17. any() :- Returns true if any value statisfies from a list of values.
"""""
print()
print("EG:-17.")
n = [ 4, 5, 1]          #All true
print(any( n ))

n = [ 1, 0, 6, 7, False]        # 0 and false are false, rest are true.
print(any( n ))
print()
'''
18. print(.ljust(width,'') OR print(.ljust(width) :- Used to print anything we want on the left side.
 '''
print("EG:-17.")
width = 20
print ('HackerRank'.ljust(width,'-'))
print ('HackerRank'.ljust(width))

'''
19. print(.rjust(width)) :- Prints to the right side.
20. print (.center(width)):- Print to the center.
EG:- H pattern

21. .fill(variable,width):- Import textwrap. It cuts the string acc to the width given. NOTE:- It'll not cut any
                            string into half, rather it'll print on the next line. 
                           
22. .wrap(variable,width):- Import textwrap. This will convert a string into a list. 
'''
print()
print("EG:-22.")
import textwrap
string = "This is a very very long string."
print (textwrap.wrap(string,5))             # Here it could've printed Thisi in first line, but it doesnt cut the
                                            # word. Therefore 'is' is written on the next line.
print (textwrap.fill(string,5))
