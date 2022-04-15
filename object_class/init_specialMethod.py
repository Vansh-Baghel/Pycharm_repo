class comp():
    def __init__(self):         #it'll be executed automatically
        print("LEES GO")

    def config(self):
        print("HI","PRO")

c1=comp()

comp.config(c1)

class comppp():
    def __init__(self,cpu,ram):         #cpu and ram are 2 different arguments
        self.cpu=cpu                    #we assign the argument to the method therefore for linking we use self.
        self.r=ram                      #LHS ie method can have any name

    def config(self):
        print("Config is: ",self.cpu, self.r)   #to print, print the method side to get the answer

req1=comppp("i5",16)        #i5 will go as cpu and 16 as ram & dont need colons for int values .
req2=comppp("i9",8)

comppp.config(req1)         #init will be automatically be printed
comppp.config(req2)


