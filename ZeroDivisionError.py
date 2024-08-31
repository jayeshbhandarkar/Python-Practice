# 29) WAP to raise the Zero Division Error

try:
    a=int(input("\n\n Enter Numerator: "))
    b=int(input("\n\n Enter Denominator: "))
    
    print("\n\n Result is",a/b)

except ZeroDivisionError:
    print("\n\n Zero Division Exception occured")
    
print("\n\n Program Ends")