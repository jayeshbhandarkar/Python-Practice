# 26) WAP to demonstrate Method Overloading.

class Student:
    def hello(self,name=None):
        if name is not None:
            print("\n\n Hello",name)
            
        else:
            print("\n\n Hello")
            
std=Student()
std.hello()
std.hello('Jayesh')