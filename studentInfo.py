# 19) WAP to read and display students information using two classes using single inheritance

class Person:
    def __init__(self,name,age,college):
        self.name = name
        self.age = age
        self.college = college
        
class Student(Person):
    def __init__(self,name,age,college,std,rollno,marks):
        Person.__init__(self,name,age,college)
        self.std = std
        self.rollno = rollno
        self.marks = marks
        
    def display(self):
        print("\n\n Student Information:\n","\n\n Name: ",self.name,"\n\n Age: ",self.age,
              "\n\n College: ",self.college,"\n\n Class :",self.std,"\n\n Roll No.: ",self.rollno,
              "\n\n Marks: ",self.marks)
        
s = Student("Jayesh",19,"SSVPS Poly","TY-CO",4,89)
s.display()

        

        
        
        
    