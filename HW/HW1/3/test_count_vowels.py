import unittest
from count_vowels import count_vowels

class TestCountVowels(unittest.TestCase):
    def assertEqualWithMessage(self, actual, expected):
        self.assertEqual(actual, expected, msg=f"\n\nExpected: {expected}\n\nActual:   {actual}")

    def test_normal_case(self):
        self.assertEqualWithMessage(count_vowels("Hello World"), 3)

    def test_empty_string(self):
        self.assertEqualWithMessage(count_vowels(""), 0)

    def test_single_word(self):
        self.assertEqualWithMessage(count_vowels("Python"), 1)

    def test_all_vowels(self):
        self.assertEqualWithMessage(count_vowels("aeiou"), 5)

    def test_case_insensitive(self):
        self.assertEqualWithMessage(count_vowels("AEIOU"), 5)

    def test_numbers_and_symbols(self):
        self.assertEqualWithMessage(count_vowels("12345!@#$%"), 0)

    def test_mixed_characters(self):
        self.assertEqualWithMessage(count_vowels("a1e2i3o4u5"), 5)

    def test_long_string(self):
        self.assertEqualWithMessage(count_vowels("a" * 1000), 1000)

    def test_no_vowels(self):
        self.assertEqualWithMessage(count_vowels("bcdfghjklmnpqrstvwxyz"), 0)

    def test_pangram(self):
        self.assertEqualWithMessage(
            count_vowels("The quick brown fox jumps over the lazy dog"),
            11
        )

if __name__ == "__main__":
    unittest.main()