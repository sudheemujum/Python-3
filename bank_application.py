class Customer:
    '''Customer class developed by Sudhee Mujamadar'''

    bankname='SUDHEEBANK'

    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance+amount
        print('Balance after deposit is:',self.balance,end='\n')

    def withdraw(self,amount):
        if amount>self.balance:
            print('Insufficient funds, cannot perform this operation')
        else:
            self.balance=self.balance-amount
            print('Balance after withdrawal is:',self.balance)

print('Welcome to',Customer.bankname)

name=input('Enter your name:')
c=Customer(name)

while True:
    print('d-Deposit \nw-Withdrawal \ne-Exit\n')
    option=input('Choose your option:')
    if option.lower()=='d':
        amount=float(input('Enter amount to deposit:'))
        c.deposit(amount)
    elif option.lower()=='w':
        amount=float(input('Enter the amount to withdraw:'))
        c.withdraw(amount)
    elif option.lower()=='e':
        print('Thank you for banking')
        break
    else:
        print('Invalid option, please choose valid option')

        
        
