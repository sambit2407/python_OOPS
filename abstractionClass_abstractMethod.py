""" When you want to create a base class and you want some methods should(must) be there in all inherited classes that you
are building """
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def printArea(self):
        pass


class Rectangle(Shape):
    type = 'rectangle'
    sides = 4

    def __init__(self, len, brt):
        self.length = len
        self.breadth = brt

    def printArea(self):# if you dont create method using printArea(name as per base class) -->TypeError: Can't
        # instantiate abstract class Rectangle with abstract method printArea
        print(self.length * self.breadth)

rec=Rectangle(20,30)
rec.printArea()