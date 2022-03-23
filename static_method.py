"""Static method is a utility method where there is no need for instance variable and static(class level) variables"""


class SamMath:
    @staticmethod
    def add(a, b):
        print('Addition is : ', a + b)

    @staticmethod
    def product(a, b):
        print('Product  is : ', a * b)

    @staticmethod
    def avg(a, b):
        print('Average is : ', (a + b) / 2)


SamMath.add(30,5)
SamMath.product(10,4)
SamMath.avg(45,35)