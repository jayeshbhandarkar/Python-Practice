# 24) WAP to demonstrate Data Hiding

class Counter:
    __count=0
    
    def getcount(self):
        self.__count+=1
        print("Count=",self.__count)
        
c=Counter()
c.getcount()

#print(c.__count)

print(c._Counter__count)