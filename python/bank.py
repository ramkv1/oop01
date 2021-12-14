import sys
class Customer:
    '''Customer class with banjk related operation'''
    bankname='DURGABANk'

    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance

    def deposite(self,amt):
        self.balance=self.balance+amt
        print('After deposit the balance:',self.balance)

    def withdraw(self,amt):
        if amt>self.balance:
            print('insufficent balance..')
            sys.exit
        self.balance=self.balance-amt
        print('After withdraw the balance:',self.balance)
        
print('Welcome to',Customer.bankname)
name=input('Enter your name')
c=Customer(name)
while True:
    print("d-deposit\nw-withdraw\ne-exit")
    option=input('choose your option:')
    if option=='d' or option=='D':
        amt=float(input('Enter The Amount to deposit'))
        c.deposite(amt)

    elif option=='w' or option=='W':
        amt=float(input('Enter Amount to withdraw'))
        c.withdraw(amt)

    elif option=="e" or option=='E':
        print('Thank you for banking')
        sys.exit

    else:
        print('choose valid option') 