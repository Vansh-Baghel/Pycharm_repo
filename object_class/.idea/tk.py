from tkinter import *

root = Tk()
frame = Frame()

root.geometry("300x200")

btn = Button(root, text="Hello World")
btn.pack()

Button1 = Checkbutton(root, text="Tutorial")

Button2 = Checkbutton(root, text="Student")

Button3 = Checkbutton(root, text="Courses")

Button1.pack()
Button2.pack()
Button3.pack()

root.mainloop()