
from physics import *
import unittest


class SpeedTestCase(unittest.TestCase):
    def test_one(self):
        res = speed(10, 2)
        res_test = 20
        self.assertEqual(res_test, res)

    def test_two(self):
        res = speed(2310, 201)
        res_test = 464310
        self.assertEqual(res_test, res)

    def test_three(self):
        res = speed(10.246, 2.354)
        res_test = 24.02687
        self.assertEqual(res_test, res)


if __name__ == "__main__":
    unittest.main()
