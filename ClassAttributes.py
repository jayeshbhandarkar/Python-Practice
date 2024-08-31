# 22) WAP to display class attributes

class Employee:
    "This is the Employee class"
    empcount=0
    
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empcount+=1
        
    def count():
        print("\n\n Count in Employee= ",Employee.empcount)
        
e1=Employee("John",1000)
print("\n\n Name: ",e1.name,"Salary: ",e1.salary)
Employee.count()
e2=Employee("Harry",2000)
print("\n\n Count outside Employee",Employee.empcount)

print("\n\n __doc__ : ",Employee.__doc__)
print("\n\n __dict__ : ",Employee.__dict__)
print("\n\n Class Name : ",Employee.__name__)
print("\n\n Module Name : ",Employee.__module__)
print("\n\n Bases : ",Employee.__bases__)