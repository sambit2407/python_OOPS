# ref -youtube(codeWithHarry)- Super() and Overriding In Classes | Python Tutorials For Absolute Beginners In Hindi #65
class A:
    class_var1 = 'i am static variable for class A'

    def __init__(self):
        self.var1 = 'I am instance variable of class A'
        self.class_var1 = 'I am class_var1 in instance method of class A'
        # if i want to access this special variable from  object class B
        self.special = 'special'


class B(A):
    # Attribute overriding
    class_var1 = 'I am static variable of class B'

    """method overriding - in order to access parent class same constructor variable we have to use super() else 
    there is no existence of parent constructor """
    def __init__(self):
        super().__init__()
        self.var1 = 'I am instance variable of class A'
        self.class_var1 = 'I am class_var1 in instance method of class B'


obj = B()
"""First this variable will be searched in child instance variable then parent instance variable then if it does not 
find it will go to child class level and then it will got parent class level """
print(obj.class_var1)
print(obj.special)
