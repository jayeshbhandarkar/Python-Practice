# 4) WAP to find the repeated items of a list

l1=[1,2,3,4,5,2,3,4,7,9,5]
l2=[]

for i in l1:
    if i not in l2:
        l2.append(i)
        
    else:
        print("\n\n", i, end=" ")