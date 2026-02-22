import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertAlmostEqual(calculator.add(2.5, 3.1), 5.6)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 5), 5)
        self.assertEqual(calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(4, 5), 20)
        self.assertEqual(calculator.multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertAlmostEqual(calculator.divide(7, 3), 2.3333333, places=6)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(5, 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            calculator.add("a", 5)
        with self.assertRaises(TypeError):
            calculator.divide(5, "b")

if __name__ == "__main__":
    unittest.main()
