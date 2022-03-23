""" polymorphism- one thing that behaves in a different ways -poly : many morphism : forms
Types :   >> operator overloading >>method overloading >> method overriding"""

"""operator overloading"""
'_____________________________'

a = 4
b = 5
c = "sambit"
"""can not add intger with string so basically when ever we use add operator for int object means we calling int 
class """
print(a + b)
"""so we can do the same operation in int class add method"""
print(int.__add__(a, b))

a = '3'
d = '4'
print(a + d)
print(str.__add__(a, d))

"""Magic Methods"""
"""When we type '+' operator it usually cal __add__() ,here actually we are passing different argument to it so we 
have to build predefined magic methods for ours """

class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2

        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        if r1>r2:
            return True
        else:
            False


sambit = Student(94, 87)
rahul = Student(96, 97)
# total = sambit + rahul  # TypeError: unsupported operand type(s) for +: 'Student' and 'Student'
"""Like there is int and str class __add__(self,other) method is predefined so for here if we arae adding + operator 
it is not defined we have to define in class """
total = sambit + rahul  # -->> Student.__add__(sambit,rahul)
print(total.m1)

"""we need to create greater than method to overload this operator because it is supported for integer as it is predefined"""
if sambit > rahul:  # TypeError: '>' not supported between instances of 'Student' and 'Student'
    print('Sambit winss')
else:
    print('Rahul winss')

