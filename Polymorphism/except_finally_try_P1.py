# 3 types of errors:- 1.Compile time error   2.Logical error     3.Run time error
# 1.Compiler time error:-Syntax errors.
# 2. Logical error:- Wrong output.
# 3. Run time error:- When user puts the wrong input.

a = 5
b = 0
try:                # It'll try & if the stmt shows any error, only then it'll read except.
    print (a/b)

except Exception as e:   # Due to this, the error wont take place and the exception stmt will be printed.
    print ("Hey, You cannot divide a Number by Zero,",e)   # e is not compulsory but it is an inbuild method
                                                           # to check whats the error

print ("Bye")

