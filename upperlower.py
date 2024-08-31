# 12) WAP with function that accepts a string and calculates the number of uppercase and lowercase characters.

def upperlower(str):
    upr=0
    lwr=0
    
    for x in str:
        if x.isupper():
            upr+=1
        
        elif x.islower():
            lwr+=1
            
        else:
            pass
    
    print("\n\n Uppercase : ",upr,"\n\n Lowercase : ",lwr)
    
str = input("\n\n Enter any String : ")
upperlower(str)