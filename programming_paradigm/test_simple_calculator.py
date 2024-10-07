import unittest
from simple_calculator import SimpleCalculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_substract(self):
        self.assertEqual(self.calc.add(6, 3), 3)

    def test_multiply(self):
        self.assertEqual(self.calc.add(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calc.add(10, 5), 2)


if __name__ == '__main__':
    unittest.main()
