# 10) WAP with functions that takes a number as parameter and checks if it is prime or not

def prime(no):
    flag = 0
    i = 2
    while i<=no//2:
        if no%i==0:
            flag = 1
            break
        i+=1
        
    if flag == 0:
        print("\n\n Number is Prime")
        
    else:
        print("\n\n Number is Not Prime")
        
no = int(input("\n\n Enter Number : "))
prime(no)
