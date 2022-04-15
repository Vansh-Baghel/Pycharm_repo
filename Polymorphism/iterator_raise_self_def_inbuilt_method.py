#iterator have some inbuilt methods which we use during projects.
nums=[7,8,9,5]

it=iter(nums)       #Address print krta h ye code.To print values,
print(it)

print(it.__next__())      #__next__ is a method which simply goes on the next value.
print(next(it))           #This is just another way of writing the previous line.

print()

for i in nums:
    print(i)

print("Here we made our own methods which does the work  as inbuilt methods")
class TopTen:
    def __init__(self):
         self.num=1         #start value will be 1

    def __iter__(self):
        return self         #as the value increments, the iter value will change automatically and does the work.

    def __next__(self):
        if self.num<= 10:
             val = self.num     #we cant return the incrementing self ka value, issilye first store it then
                                #return the stored value.
             self.num+=1        #incrementing

             return val
        else:                   #else condition nhi hoti toh it would've returned none value till the infinity.
                                #but the raise stmt stopped the further execution of it.
            raise StopIteration #raise stops the error which we notice, & stopiteration is an inbuilt method.
values = TopTen ()
for i in values:
    print (i)
