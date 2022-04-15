#Types of variables:- Two types...

#1.Class(Static) variables:- It'll affect all the objects/variable in the class.
#2.Instance variable:- It'll just affect that particular object/variable.
#Namespace:- Where we create the variable/object.

class Cars:
    Wheels=4                    #Class variable
    def __init__(self):
        self.model="Ferrari"    #Instance variable.
        self.color="Red"

c1=Cars()
c2=Cars()

print(c1.model,c1.color,c1.Wheels,c2.model,c2.color,c2.Wheels)

Cars.Wheels=5           #Class variable mai change.
                        #Changes for all objects therefore changed for the init.
Cars.color="Blue"       #Color will not change,as color doesnt belong to class variable.
c1.color="Unique"       #Instance variable mai change
                        #Color changes as a particular variable is mentioned so the change is direct into the
                        #init wala stmt.

print(c1.model,c1.color,c1.Wheels,c2.model,c2.color,c2.Wheels)