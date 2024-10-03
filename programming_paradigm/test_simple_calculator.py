from simple_calculator import SimpleCalculator
import unittest

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        result = self.calc.add(1, 1)
        self.assertEqual(result, 2)

    def test_subtraction(self):
        result = self.calc.subtract(1, 1)
        self.assertEqual(result, 0)

    def test_multiply(self):
        result = self.calc.multiply(1, 1)
        self.assertEqual(result, 1)

    def test_divide(self):
        result = self.calc.divide(1, 1)
        self.assertEqual(result, 1)

        result2 = self.calc.divide(1, 0)
        self.assertIsNone(result2)
