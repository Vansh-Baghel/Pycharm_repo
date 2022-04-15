n = int(input("Enter number of input numbers"))
print(n)
student_marks = {}                                      # syntax for dict
for _ in range(n):                                      # _ determines the previous value.
    x=name, *scores = input("Enter name and mrks").split()  # split is used to separate the string into list ie
                                                        # continue values to single list.

    scores = list(map(float,scores))                    # used to convert the input of line into float value.
                                                        # map is used to iterate each value one by one.
                                                        # list provides values to the scores. otherwise just the
                                                        # address of map object will be printed.

    student_marks[name] = scores                        # means name will be the key and list of score is its
                                                        # value.EG:- {"Vansh": 21.3,53.0,42.0}.
    print(x)
input_name = input()                                    # for this name, we will find the avg.

marks = student_marks[input_name]                       # student_marks["Vansh"]=21.3 ,53.0, 42.0.
print(marks)                                            # Here, mrks in the form of list will be printed as we used
                                                        # list, warna object ka address milta.
# Syntax for format--> format(value,'.nf') where n is the nos. after decimal. nf is basically the format specifier.
print(format(sum(marks) / 3, '.2f'))                    # sum (iterable)

add=0                                                   # Another method to print the avg.
avg=0.0
for i in marks:
    add+=i
    avg=(add)/3

print("{0:.2f}".format(avg))                            # Syntax--> { } .format(value)
