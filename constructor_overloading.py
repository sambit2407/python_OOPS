"""Method Overloading - When same method name is used  but in different argument
    So in constructor overloading we are used two constructor with different argument (which is invalid)"""

"""So if there is method overloading happens ,PVM will execute the Last method """
class Test:
    """So due to overloading this method(constructor) will not be executed"""
    def __init__(self):
        print('First constructor')
    """As this is the last one python will execute this method(constructor) only"""
    def __int__(self, x):
        print('second constructor')


#obj = Test()#typeError-as it is executing last method we have to add argument for the constructor
obj=Test(10)
