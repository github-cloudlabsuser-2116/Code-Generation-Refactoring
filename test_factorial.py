import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_one(self):
        self.assertEqual(factorial(1), 1)

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

    def test_factorial_large(self):
        self.assertEqual(factorial(10), 3628800)

    def test_factorial_invalid(self):
        with self.assertRaises(RecursionError):
            factorial(-1)

if __name__ == '__main__':
    unittest.main()

# We recommend installing an extension to run python tests.