class Bank:
    bank_name='SAMBIT-BANK-PVT.LTD'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def deposit(self,balance):

        self.balance=self.balance+balance
        print(f'Your account balance after deposit is{self.balance}')

    def check_balance(self):
        print(f"Your current Account balance is {self.balance}")

    def withdraw(self,balance):
        if self.balance<balance:
            print("Insufficient funds!!")
        else:
            self.balance=self.balance-balance



name=input('Please Enter your name')

bank=Bank(name)
print(f'Hi {name}Welcome to {Bank.bank_name}')
while True:
    inp=input('Chose Option --->>\nd-Deposit\nw-Withdraw\nc-CheckBalance\nq-Quit\n ')

    if inp.lower()=='d':
        balance=float(input('Enter Amount to deposit : '))
        bank.deposit(balance)
    elif inp.lower()=='w':
        balance=float(input('Enter Amount to withdraw : '))
        bank.withdraw(balance)
    elif inp.lower()=='c':
        bank.check_balance()
    elif inp.lower()=='q':
        print(f'Thanks for Visiting {Bank.bank_name}')
        break
    else:
        print('Please select  Valid option. ')









