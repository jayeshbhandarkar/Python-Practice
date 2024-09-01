import sys
from abc import ABC, abstractmethod

class BankAccount:
    def __init__(self):
        self.name=None
        self.accno=None
        self.balance=None

    def inputCustData(self):
        self.name = input("Enter Name: ")
        self.accno = input("Enter Account No: ")
        self.balance = int(input("Enter Balance: "))

    def showCustData(self):
        print("Name of Account Holder: ",self.name)
        print("Account No: ",self.accno)
        print("Balance: ",self.balance)

    def deposit(self):
        pass

    def withdraw(self):
        amt = int(input("Enter Amount: "))
        if amt <= self.balance:
            self.balance -= amt
        else:
            print("Insufficient Balance")

class SavingAccount(BankAccount):
    def deposit(self):
        amt = int(input("Enter Amount: "))
        self.balance+=amt

    def withdraw(self):
        amt = int(input("Enter Amount: "))
        if self.balance-amt < 1000:
            print("Insufficient Balance")
        else:
            self.balance -= amt

    def getInterest(self,rate):
        interest = (rate/100)*self.balance
        print("Interest of Saving Account",interest)

class CurrentAccount(BankAccount):
    def deposit(self):
        amt = int(input("Enter Amount: "))
        self.balance+=amt

    def withdraw(self):
        amt = int(input("Enter Amount: "))
        if amt <= self.balance:
            self.balance -= amt
        else:
            print("Insufficient Balance")

    def getInterest(self,rate):
        interest = (rate/100)*self.balance
        print("Interest of Saving Account",interest)

class Interest1(SavingAccount):
    def setInterest(self):
        super().getInterest(2)

bank = SavingAccount()

while True:
    print("\n")
    print("1. Input Data")
    print("2. Display Data")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Saving Account Interest")
    print("6. Current Account Interest")
    print("7. Exit")

    print("\n")
    ch = int(input("Enter Any Choice: "))
    if ch==1:
        bank.inputCustData()

    elif ch==2:
        bank.showCustData()

    elif ch==3:
        bank.deposit()

    elif ch==4:
        bank.withdraw()

    elif ch==5:
        bank.getInterest(4)

    elif ch==6:
        bank.getInterest(2)

    elif ch==7:
        sys.exit()

    else:
        print("Invalid Input")
