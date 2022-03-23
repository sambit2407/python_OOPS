"""Instance Variable - For every object or instance this instance variable is created and and these are different for
every instances """

"""static variable - It is a class level variable , for every instance of the class this variable is same  so to 
unnecessarily create same variable for every object we create static variable which will be same for every instance. """

"""Local variable - to meet the temporary requirements of the developer it is declared inside methods"""


class School:
    """It is static variable as it is same for all the instances created"""
    school_name = ' Kaliga High School'  # static avriable

    """it is a instance variable as it will be different for every object created"""

    def __init__(self, name, rollno):
        self.name = name  # instance variable
        self.rollno = rollno  # instance variable

    def info(self):
        """it is a local variable as it is declared in the method for meet requirements """
        x = 10  # local variable
        for i in range(x):
            """i is also local variable"""
            print(i)
