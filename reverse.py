# 1) WAP to display the reverse of a number.

n = int(input("\n\n Enter any Number : "))
rev = 0

while(n>0):
    rem = n%10
    rev = rev*10+rem
    n = n//10
    
print("\n\n Reverse of a Number = ",rev)