# 25) WAP to demonstrate method overriding

class Bird:
    def __init__(self):
        print("\n Bird Ready")
        
    def who(self):
        print("\n I am a Bird")
        
    def swim(self):
        print("\n I can swim")
        
class Penguin(Bird):
    def __init__(self):
        print("\n Penguin Ready")
        
    def who(self):
        super().who()
        print("\n I am a Penguin")
        
    def run(self):
        print("\n I can run")
        
p = Penguin()
p.who()
p.swim()
p.run()