"""single Inheritance"""

class A:
    def m1(self):
        print('i am in parent class method')


class B(A):
    def m2(self):
        print('I am in child class method')


obj = B()  # child class
obj.m1()
obj.m2()  # can operate parent class methods

"""Multi level inheritance"""
class A:
    def m1(self):
        print('I am in parent class')

class B(A):
    def m2(self):
        print('I am in child class')

class C(B):
    def m3(self):
        print('I am in Sub child class')

obj1=C()
obj1.m1()
obj1.m2()
obj1.m3()

"""Multiple Inheritance"""
class A:
    def m1(self):
        print('I am in Parent1 method')

class B:
    def m1(self):
        print('I am in Parent2 method')

class C(B,A):#if same method name in both the parents then which ever parent name given first that method will run first
    def m3(self):
        print('I am in child method')

obj2=C()
obj2.m3()
#obj2.m2()
obj2.m1()
