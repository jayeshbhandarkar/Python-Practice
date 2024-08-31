# 8) WAP to combine values of two dictionaries having similar keys and create a new dictionary.

from collections import Counter
d1 = {'a':100,'b':200, 'c':300}
d2 = {'a':300,'b':200, 'd':400}

a = Counter(d1)
b = Counter(d2)
c = a+b
print(c)