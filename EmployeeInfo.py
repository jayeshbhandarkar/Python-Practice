# 18) WAP to create a class Employee with data members: name, department and salary. Create methods for reading and
# printing employee information.

class Employee:
    def get(self):
        self.name = input("\n Enter Name : ")
        self.dept = input("\n Enter Dept.: ")
        self.salary = int(input("\n Enter Salary : "))
        
    def put(self):
        print("\n\n ------Employee Information------")
        print("\n Name : ",self.name)
        print("\n Dept.: ",self.dept)
        print("\n Salary : ",self.salary)
        
e = Employee()
e.get()
e.put()