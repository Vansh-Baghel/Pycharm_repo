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

except ZeroDivisionError as e:                  #ZeroDivisionError is the keyword to locate the error based on 0.
                                                #If the value of b is zero, the k input wont be executed bcoz
                                                #the control will go to except after the error stmt.
    print("Hey, You cannot divide a Number by Zero")

except ValueError as e:             #ValueError shows the error when the input datatype is different.
    print("Invalid Input")

except Exception as e:              #Exception is used for all types of error & to be on safer side we always
                                    #use it in the end.
    print("Something went Wrong...")


finally:                            # This keyword will be executed after both try and except stmts.
                                    # We req this to close the try and except stmts.
     print ("resource Closed")