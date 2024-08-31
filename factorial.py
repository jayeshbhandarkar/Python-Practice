# 11) WAP with function to calculate the factorial of a given number.

def fact(no):
    if no == 1:
        return no
    
    else:
        return no*fact(no-1)
    
no = int(input("\n\n Enter any Number : "))
print(fact(no))