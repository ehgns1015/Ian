import unittest
from remove_duplicates import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):
    def assertEqualWithMessage(self, actual, expected):
        self.assertEqual(actual, expected, msg=f"\n\nExpected: {expected}\n\nActual:   {actual}")

    def test_with_duplicates(self):
        self.assertEqualWithMessage(remove_duplicates([1, 2, 2, 3, 1]), [1, 2, 3])

    def test_without_duplicates(self):
        self.assertEqualWithMessage(remove_duplicates([1, 2, 3]), [1, 2, 3])

    def test_with_strings(self):
        self.assertEqualWithMessage(remove_duplicates(["a", "b", "a", "c"]), ["a", "b", "c"])

    def test_empty_list(self):
        self.assertEqualWithMessage(remove_duplicates([]), [])

    def test_single_element(self):
        self.assertEqualWithMessage(remove_duplicates([42]), [42])

    def test_all_duplicates(self):
        self.assertEqualWithMessage(remove_duplicates([7, 7, 7, 7]), [7])

    def test_numbers_and_strings(self):
        self.assertEqualWithMessage(remove_duplicates([1, "1", 1, "1"]), [1, "1"])

    def test_mixed_types(self):
        self.assertEqualWithMessage(remove_duplicates([1, "a", 1, "a", 2, "b"]), [1, "a", 2, "b"])

    def test_case_sensitive_strings(self):
        self.assertEqualWithMessage(remove_duplicates(["A", "a", "A", "a"]), ["A", "a"])

    def test_large_list(self):
        input_list = list(range(1000)) + list(range(500))
        expected_output = list(range(1000))
        self.assertEqualWithMessage(remove_duplicates(input_list), expected_output)

    def test_with_none_values(self):
        self.assertEqualWithMessage(remove_duplicates([None, None, 1, None, 1]), [None, 1])

if __name__ == "__main__":
    unittest.main()

