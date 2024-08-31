# 2) WAP to check if given number is palindrome or not.

num = int(input("\n\n Enter any Number : "))

n = num
rev = 0

while num>0:
    rem = num%10
    rev = rev*10+rem
    num = num//10
    
if n == rev:
    print("\n\n Number is Palindrome")
    
else:
    print("\n\n Number is Not Palindrome")

