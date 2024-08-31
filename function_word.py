# 13) WAP with function to find the smallest and largest word in a given string

def check(str):
    list = []
    estr = " "
    str = str + " "
    
    for x in range(len(str)):
        if(str[x]==" "):
            list.append(estr)
            estr = " "
            
        else:
            estr += str[x]
            
    min = len(list[0])
    max = len(list[0])
    
    for x in list:
        if(len(x) < min):
            min = len(x)
            
        if(len(x) > max):
            max = len(x)
            
    return min,max

str = "Hello Welcome to Python Programming"
min,max = check(str)
print("\n\n Smallest word length : ",min,"\n\n Largest word length : ",max)