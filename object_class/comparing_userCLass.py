class comp:
    def __init__(self):
        self.age=19
        self.name='Vansh'

    def update(self):
        self.age = 151

    def compare(self, other):
        if self.age == other.age:
            return True

c1=comp()           #note that there is no argument in the self so comp ka bracket will be empty.
c2=comp()
c1.name="Updated"
print("Direct class ki value: ",c1.name,c1.age,c2.name,c2.age,)

comp.update(c1)             #c1 update() bhi chalega
print(c1.age)

if c1.compare(c2):          #for comparing the syntax---> (first.compare.second)
    print("Same age")
else:
    print("Different age")




