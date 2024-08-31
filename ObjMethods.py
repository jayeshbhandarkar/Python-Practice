# 23) WAP to Access Object Methods

class Person:
    "This is Person class"
    
    def __init__(self,name,age): 
        self.name=name
        self.age=age
        
        print(" Person Created: ",self.name)
        
    def myfunc(self):
        print("\n\n Hello My Name is "+self.name)
        print("\n\n My Age is ",self.age)
        
p1=Person("John",30)
p1.myfunc()