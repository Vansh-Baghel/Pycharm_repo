# 1. write a program to read first 5 characters from the file in python

ANS:

```Python
def read_first_five_characters(file_path):
    try:
        with open(file_path, 'r') as file:
            first_five_chars = file.read(5)
            return first_five_chars
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("Error reading the file.")

# Example usage
file_path = 'example.txt'  # Replace with your file path
result = read_first_five_characters(file_path)
print(result)
```

# 2. which function of mysql.connector in python is used to open a connection to database

ANS:

```Python
import mysql.connector

# Establishing a connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost",   # Replace with your host
    user="username",    # Replace with your username
    password="password",  # Replace with your password
    database="mydatabase"  # Replace with your database name
)

# Perform database operations...

# Closing the connection
connection.close()

```

# 3. Button using tkinter

```Python
from tkinter import *

root = Tk()
frame = Frame()

root.geometry("300x200")

btn = Button(root, text="Hello World")
btn.pack()

root.mainloop()
```

# 4. CheckBox using tkinter

```Python
from tkinter import *

root = Tk()
frame = Frame()

root.geometry("300x200")

Button1 = Checkbutton(root, text="Tutorial")

Button2 = Checkbutton(root, text="Student")

Button3 = Checkbutton(root, text="Courses")

Button1.pack()
Button2.pack()
Button3.pack()

root.mainloop()
```

# 5. lambda function is also known as anonymous function in python, Justify

- The lambda keyword is used to define anonymous functions in Python. Usually, such a function is meant for one-time use.
- **No explicit name**: Unlike regular functions defined using the def keyword, lambda functions do not require a specific name
- **Concise and inline**
- **Limited scope and visibility**: Lambda functions are typically used in a limited context and have a restricted scope. They are not designed to be reusable or accessible from other parts of the codebase

```Python
square = lambda x : x * x
n = square(5)  #calling lambda function

greet = lambda name: print('Hello ', name)
greet('Steve')  #output: Hello Steve

```

# 6. Text files and binary files in python

- Text files are files that contain **plain text characters** encoded in a specific character encoding, such as ASCII or UTF-8.
- Text files can be opened and read using the built-in **open()** function.
- When reading from a text file, the **data is returned as a string or a sequence of strings** representing the lines of text in the file.
- When writing to a text file, you can use the **write()** method to write strings or a sequence of strings to the file.

Binary Files:

- Binary files are files that contain non-textual data, such as images, audio, video, or serialized objects.
- Binary files can be opened and read using the open() function.
- When reading from a binary file, the data is returned as a sequence of bytes or byte arrays.
- When writing to a binary file, you can use the write() method to write bytes or byte arrays to the file.

```Python
# Reading from a text file
with open('example.txt', 'r') as text_file:
    contents = text_file.read()
    print(contents)

# Reading from a binary file
with open('example.bin', 'rb') as binary_file:
    contents = binary_file.read()
    print(contents)

```

# 7. Try and except in python

```Python
def div(a , b):
    if (a < 10):
        print("Smaller than 10")
    print(a/b)

try:
    div(1, 0)

except ZeroDivisionError:
    print("Zero Div Error occured")

```

# 8. Raising exception in python

```Python
def div(a , b):
    if (a < 10):
        raise ValueError("Age smaller")
    print(a/b)

try:
    div(1, 0)

except ZeroDivisionError:
    print("Zero Div Error occured")

```

# 9. Constructor, class, object

```Python
class Employee:

    def __init__(self, age, name):
        self.age = age;
        self.name = name;

    def displayName(self):
        print(f"Employee name is: {self.name}");

emp = Employee(10, "Vansh")
emp.displayName()

```

# 10. Polymorphism

```Python
def add (a, b, c=0):
    print(f"Addition is {a + b + c}")

add(1,2)
add(1,2,3)

```
