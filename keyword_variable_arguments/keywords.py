def person(name,**data):     #we use double stars to get the input with keywords.
    print(name)
    print(data)

person("Vansh",age=18,city="Bhy",mob=3489)     #here you are using keywords to describe your values

#Another way
def cars(model,**color):
    print(model)
    for i,j in color.items():   #i,j refers to key and value resp.; & items is a function.
        print(i,j)

cars("idk",a="pink",b="blue",c="red")



