# 3) WAP to create a list and demonstrate any four list methods.

lst1 = [10,20,30,40,50]
print("\n\n The Given List1 is ",lst1)

lst2 = [60,70,80,90,100]
print("\n\n The Given List2 is ",lst2)

lst1.append(55)
print("\n\n List after Appending is ",lst1)

lst1.insert(3,35)
print("\n\n List after Inserting an element is ",lst1)

lst1.extend(lst2)
print("\n\n List after Extending is ",lst1)

lst2.reverse()
print("\n\n List after Reversing is ",lst2)