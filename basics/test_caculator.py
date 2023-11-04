import unittest
from unittest.mock import patch

import calculator


class CalculatorTestDualMode(unittest.TestCase):
    @patch('calculator.input_read', return_value=[1, 2])
    def test_addOperation(self, input):
        self.assertEqual(3, calculator.add())

    @patch('calculator.input_read', return_value=[2, 2])
    def test_divOperation(self, input):
        self.assertEqual(1, calculator.div())

    @patch('calculator.input_read', return_value=[4, 2])
    def test_subtractionOperation(self, input):
        self.assertEqual(2, calculator.sub())

    @patch('calculator.input_read', return_value=[5, 2])
    def test_multiplyOperation(self, input):
        self.assertEqual(10, calculator.mul())


if __name__ == '__main__':
    unittest.main()
