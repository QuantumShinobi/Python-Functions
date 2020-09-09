import unittest
from unittest import result
from figures import *


class SquareTestCase(unittest.TestCase):

    def test_area(self):
        square = Square(10)
        area = 100
        self.assertEqual(area, square.area())

    def test_perimeter(self):
        square = Square(10)
        perimeter = 40
        self.assertEqual(perimeter, square.perimeter())


class RectangleTestCase(unittest.TestCase):

    def test_area(self):
        rectangle = Rectangle(10, 20)
        area = 200
        self.assertEqual(area, Rectangle.area())

    def test_perimeter(self):
        rectangle = Rectangle(10, 20)
        perimeter = 60
        self.assertEqual(perimeter, Rectangle.perimeter())


if __name__ == "__main__":
    unittest.main()
