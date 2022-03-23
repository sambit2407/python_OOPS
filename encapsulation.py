"""Encapsulation -app amm khaye gutliya na gine , example - as we are using computer and doing required stuff but we
are not moreover aware of what is there is hard disks or what is there in mouse """
"""So basically encapsulation is encapsulating requirements in class objects methods variables without showing or 
giving hectic to the end user """


class Employee:
    no_of_leaves = 10

    def __init__(self, name, sal, role):
        self.name = name
        self.sal = sal
        self.role = role

    def printDetails(self):
        print(f'The Employee {self.name} is working as a {self.role} and getting {self.sal}')

    @classmethod
    def change_leaves(cls, leaves):
        cls.no_of_leaves = leaves
    
    @staticmethod  # utility method ,if you want anything irrespective of class and objects
    def printAnything(anything):
        print(anything)


emp = Employee('sam', 120000, 'data scienctist')
emp.printDetails()
print(Employee.no_of_leaves)
emp.change_leaves(12)
print(Employee.no_of_leaves)
emp.printAnything('I love You')
