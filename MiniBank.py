#bank name
#check balance
#deposit amount
#withdrawl
class Bank:
    '''bank name would be same for all instance(static variable)'''
    bank_name='State Bank Of India'
    #first method will run when instance is created
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance

    def check_balance(self):
        print(f'Your current account balance is : {self.balance}')

    def deposit(self,bal):
        self.balance=self.balance+bal
        print('Cash deposited successfully !!')
        print(f'After deposit Your current account balance is  {self.balance}')

    def withdraw(self,bal):
        if bal<=self.balance:
            self.balance = self.balance - bal
            print('Transaction successful !!')
        else:
            print('Insufficient Funds !!')
    @classmethod
    def change_bankName(cls):
        cls.bank_name='  Axis Bank '
    @staticmethod
    def welcome_msg():
        print(f'Welcome {name} to {Bank.bank_name} ')





name= input('Please Enter Your name : ')
person1=Bank(name)
Bank.change_bankName()
Bank.welcome_msg()


while True:
    inp=input('Please choose the option \nc : check balance \nd :deposit \nw : withdraw \nq : quit\n')
    if inp=='c':
        person1.check_balance()
    elif inp=='d':
        bal=float(input('Enter the deposit amount : '))
        person1.deposit(bal)
    elif inp=='w':
        bal=float(input('Enter the withdraw amount : '))
        person1.withdraw(bal)

    elif inp=='q':
        break

    else:
        print('please Enter valid option..')









