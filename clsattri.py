class Person:
    "This is Person class"
    
print(Person.__doc__)
print(Person.__dict__)
print(Person.__name__)
print(Person.__module__)
print(Person.__bases__)

p1=Person()
print(type(p1))