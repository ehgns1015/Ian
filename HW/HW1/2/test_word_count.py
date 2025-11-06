import unittest
from word_count import count_words

class TestCountWords(unittest.TestCase):
    def assertEqualWithMessage(self, actual, expected):
        self.assertEqual(actual, expected, msg=f"\n\nExpected: {expected}\n\nActual:   {actual}")

    def test_normal_case(self):
        self.assertEqualWithMessage(
            count_words(["apple", "banana", "apple", "orange", "banana", "apple"]),
            {'apple': 3, 'banana': 2, 'orange': 1}
        )

    def test_empty_list(self):
        self.assertEqualWithMessage(count_words([]), {})

    def test_single_word(self):
        self.assertEqualWithMessage(count_words(["one"]), {'one': 1})

    def test_all_same_word(self):
        self.assertEqualWithMessage(count_words(["a", "a", "a", "a"]), {'a': 4})

    def test_multiple_words(self):
        self.assertEqualWithMessage(
            count_words(["cat", "dog", "cat", "dog", "bird"]),
            {'cat': 2, 'dog': 2, 'bird': 1}
        )

    def test_case_sensitive(self):
        self.assertEqualWithMessage(
            count_words(["test", "test", "TEST"]),
            {'test': 2, 'TEST': 1}
        )

    def test_empty_string_words(self):
        self.assertEqualWithMessage(
            count_words(["", "", " "]),
            {'': 2, ' ': 1}
        )

    def test_numeric_strings(self):
        self.assertEqualWithMessage(
            count_words(["123", "123", "456", "123"]),
            {'123': 3, '456': 1}
        )

    def test_long_repeats(self):
        self.assertEqualWithMessage(
            count_words(["repeat"] * 5),
            {'repeat': 5}
        )

    def test_multiple_repeats(self):
        self.assertEqualWithMessage(
            count_words(["a", "b", "c", "a", "b", "c", "a", "b", "c"]),
            {'a': 3, 'b': 3, 'c': 3}
        )

    def test_mixed_types_strings(self):
        self.assertEqualWithMessage(
            count_words(["apple", "Apple", "APPLE", "apple"]),
            {'apple': 2, 'Apple': 1, 'APPLE': 1}
        )


if __name__ == "__main__":
    unittest.main()
