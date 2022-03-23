class Test:
    static_var = 100

    def __init__(self):
        print('Instance variable ', self.static_var)
        self.static_var = 3400
        print('Instance variable** ', self.static_var)

    """Static(outside of any methods of class and class level variables) variable can only be modified using class 
    name or like below in class method where we can change class attribute """

    @classmethod
    def m1(cls):
        cls.static_var = 320


# creating the object so __init__ method is invoked
obj = Test()

# creating another obj so __init__ method is invoked
obj1 = Test()
# calling the class method
obj.m1()
print(obj.static_var)
print(Test.static_var)

print(obj.__dict__)
print(obj1.__dict__)
print(Test.__dict__)
