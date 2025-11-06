import unittest
import inspect
from unittest.mock import patch
from double_factorial import double_factorial

class TestDoubleFactorial(unittest.TestCase):
    def assertEqualWithMessage(self, actual, expected):
        self.assertEqual(actual, expected, msg=f"\n\nExpected: {expected}\n\nActual:   {actual}")

    def test_zero(self):
        self.assertEqualWithMessage(double_factorial(0), 1)

    def test_one(self):
        self.assertEqualWithMessage(double_factorial(1), 1)

    def test_small_odd(self):
        self.assertEqualWithMessage(double_factorial(3), 3)

    def test_small_even(self):
        self.assertEqualWithMessage(double_factorial(4), 8)

    def test_medium_odd(self):
        self.assertEqualWithMessage(double_factorial(5), 15)

    def test_medium_even(self):
        self.assertEqualWithMessage(double_factorial(6), 48)

    def test_large_odd(self):
        self.assertEqualWithMessage(double_factorial(7), 105)

    def test_large_even(self):
        self.assertEqualWithMessage(double_factorial(8), 384)

    def test_two(self):
        self.assertEqualWithMessage(double_factorial(2), 2)

    def test_nine(self):
        self.assertEqualWithMessage(double_factorial(9), 945)

    def test_ten(self):
        self.assertEqualWithMessage(double_factorial(10), 3840)

    def test_is_recursive_implementation(self):
        """Test that the function actually calls itself (recursive implementation)"""
        with patch('double_factorial.double_factorial', wraps=double_factorial) as mock_func:
            result = mock_func(5)
            self.assertEqual(result, 15)
            # Check that the function was called more than once (recursive calls)
            self.assertGreater(mock_func.call_count, 1, 
                             "Function should call itself recursively")

    def test_no_loops_in_code(self):
        """Test that the implementation doesn't use loops (for/while)"""
        source = inspect.getsource(double_factorial)
        
        # Check for loop keywords
        self.assertNotIn('for ', source, "Implementation should not use 'for' loops")
        self.assertNotIn('while ', source, "Implementation should not use 'while' loops")
        
        # Check that function calls itself
        self.assertIn('double_factorial(', source, 
                     "Function should call itself recursively")

if __name__ == "__main__":
    unittest.main()