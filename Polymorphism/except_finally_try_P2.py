# 3 types of errors:- 1.Compile time error   2.Logical error     3.Run time error
# 1.Compiler time error:-Syntax errors.
# 2. Logical error:- Wrong output.
# 3. Run time error:- When user puts the wrong input.

a = 5
b = 2
try:
     print ("resource Open")
     print (a/b)
     k = int (input ("Enter a number"))
     print (k)

except Exception as e:
     print ("Hey, You cannot divide a Number by Zero" , e)

finally:                            # This keyword will be executed after both try and except stmts.
                                    # We req this to close the try and except stmts.
     print ("resource Closed")