# 7) WAP to create a dictionary and demonstrate any four dictionary methods.
 
dict1 = {1:"ABC",2:"PQR",3:"XYZ",4:"MNO"}
print("\n\n The Given Dictionary is : ",dict1)

dict2 = {5:"GHI",6:"STU"}
print("\n\n The Given Dictionary is : ",dict2)

dict1.update({7:"JKL"})
print("\n\n After Updating Dictionary is : ",dict1)

x = dict1.__len__()
print("\n\n Length of dictionary is : ",x)

dict1 = dict2.copy()
print("\n\n After Copying Dict2 elements to Dict1 are : ",dict1)

dict2.popitem()
print("\n\n Dictionary after pop item is : ",dict2)