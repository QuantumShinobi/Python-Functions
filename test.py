import unittest
from unittest import result
from figures import *

# tested
# 1. square
# 2 rectangle
# 3 cuboid


class SquareTestCase(unittest.TestCase):

    def test_area(self):
        square = Square(10)
        area = 100
        self.assertEqual(area, square.area())

    def test_perimeter(self):
        square = Square(10)
        perimeter = 40
        self.assertEqual(perimeter, square.perimeter())
        
    def test_diagonal(self) :
        square = Square(10)
        diagonal = ((10)**2 + (10)**2)**0.5
        self.assertEqual(diagonal, square.diagonal())


class RectangleTestCase(unittest.TestCase):

    def test_area(self):
        rectangle = Rectangle(10, 20)
        area = 200
        self.assertEqual(area, rectangle.area())

    def test_perimeter(self):
        rectangle = Rectangle(10, 20)
        perimeter = 60
        self.assertEqual(perimeter, rectangle.perimeter())


class CuboidTestCase(unittest.TestCase):
    def test_csa(self):
        cbd = Cuboid(10, 8, 7)
        #    l=8, b=7
        csa = 300
        self.assertEqual(csa, cbd.curved_surface_area())

    def test_tsa(self):
        cbd = Cuboid(10, 8, 7)
        #    l=8, b=7
        csa = 300
        self.assertNotEqual(csa, cbd.total_surface_area())


if __name__ == "__main__":
    unittest.main()
