import unittest
from unittest import result
from figures import *


class SquareTestCase(unittest.TestCase):

    def test_area(self):
        square = Square(10)
        area = 100
        self.assertEqual(area, square.area)

    def test_perimeter(self):
        square = Square(10)
        perimeter = 40
        self.assertEqual(perimeter, square.perimeter)
