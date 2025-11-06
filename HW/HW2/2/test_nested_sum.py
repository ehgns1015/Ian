import unittest
import inspect
from unittest.mock import patch
from nested_sum import nested_sum

class TestNestedSum(unittest.TestCase):
    def assertEqualWithMessage(self, actual, expected):
        self.assertEqual(actual, expected, msg=f"\n\nExpected: {expected}\n\nActual:   {actual}")

    def test_empty_list(self):
        self.assertEqualWithMessage(nested_sum([]), 0)

    def test_single_number(self):
        self.assertEqualWithMessage(nested_sum([5]), 5)

    def test_flat_list(self):
        self.assertEqualWithMessage(nested_sum([1, 2, 3]), 6)

    def test_one_level_nesting(self):
        self.assertEqualWithMessage(nested_sum([1, [2, 3], 4]), 10)

    def test_two_level_nesting(self):
        self.assertEqualWithMessage(nested_sum([1, [2, [3, 4]], 5]), 15)

    def test_all_nested(self):
        self.assertEqualWithMessage(nested_sum([[1, 2], [3, 4]]), 10)

    def test_deep_nesting(self):
        self.assertEqualWithMessage(nested_sum([1, [2, [3, [4]]]]), 10)

    def test_complex_nesting(self):
        self.assertEqualWithMessage(nested_sum([5, [10, [15, 20]], 25]), 75)

    def test_nested_empty_lists(self):
        self.assertEqualWithMessage(nested_sum([1, [], [2, []], 3]), 6)

    def test_negative_numbers(self):
        self.assertEqualWithMessage(nested_sum([-1, [2, [-3, 4]], -5]), -3)

    def test_mixed_positive_negative(self):
        self.assertEqualWithMessage(nested_sum([10, [-5, [3, -2]], 1]), 7)

    def test_very_deep_nesting(self):
        self.assertEqualWithMessage(nested_sum([[[[[1]]]], 20]), 21)

    def test_is_recursive_implementation(self):
        """Test that the function actually calls itself (recursive implementation)"""
        with patch('nested_sum.nested_sum', wraps=nested_sum) as mock_func:
            result = mock_func([1, [2, [3, 4]], 5])
            self.assertEqual(result, 15)
            # Check that the function was called more than once (recursive calls)
            self.assertGreater(mock_func.call_count, 1, 
                             "Function should call itself recursively")

    def test_no_loops_in_code(self):
        """Test that the implementation doesn't use loops (for/while)"""
        source = inspect.getsource(nested_sum)
        
        # Check for loop keywords
        self.assertNotIn('for ', source, "Implementation should not use 'for' loops")
        self.assertNotIn('while ', source, "Implementation should not use 'while' loops")
        
        # Check that function calls itself
        self.assertIn('nested_sum(', source, 
                     "Function should call itself recursively")
        
        # Check that it uses type() instead of isinstance() for beginners
        has_type_check = 'type(' in source
        has_isinstance = 'isinstance(' in source
        self.assertTrue(has_type_check or has_isinstance, 
                       "Function should check if an item is a list using type() or isinstance()")

if __name__ == "__main__":
    unittest.main()