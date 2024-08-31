# 21) WAP to implement Multilevel Inheritance

class Person:
    def __init__(self,name):
        self.name = name
        
class Employee(Person):
    def __init__(self,name,salary):
        Person.__init__(self,name)
        self.salary = salary
        
class Worker(Employee):
    def __init__(self,name,salary,workhrs):
        Employee.__init__(self,name,salary)
        self.workhrs = workhrs
        
    def display(self):
        print("\n ------Worker info------\n","\n\n Name: ",self.name,"\n\n Salary: ",self.salary,
              "\n\n Hrs: ",self.workhrs)
    
w = Worker("John",1000,5)
w.display()