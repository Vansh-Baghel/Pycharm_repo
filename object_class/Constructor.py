class Employee:

    def __init__(self, age, name):
        self.age = age;
        self.name = name;

    def displayName(self):
        print(f"Employee name is: {self.name}");

emp = Employee(10, "Vansh")
emp.displayName()
