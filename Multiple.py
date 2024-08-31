# 20) WAP to implement multiple inheritance.

class Color:
    def fun_c(this):
        print("\n\n In Color class")
        
class Shape:
    def fun_s(this):
        print("\n\n In Shape class")
        
class Box(Color,Shape):
    def fun_b(this):
        print("\n\n In Box class")
        
b = Box()
b.fun_c()
b.fun_s()
b.fun_b()