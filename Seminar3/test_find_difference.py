import unittest
from find_difference import find_the_difference


class TestDifferenceFinder(unittest.TestCase):
    def test_single_character_addition(self):
        self.assertEqual(find_the_difference("", "a"), "a")
        self.assertEqual(find_the_difference("a", "aa"), "a")

    def test_different_characters(self):
        self.assertEqual(find_the_difference("abcd", "abcde"), "e")
        self.assertEqual(find_the_difference("hello", "hellox"), "x")

    def test_repeated_characters(self):
        self.assertEqual(find_the_difference("aabbcc", "aabbbcc"), "b")
        self.assertEqual(find_the_difference("xxyyzz", "xxyyyzz"), "y")

    def test_mixed_case(self):
        self.assertEqual(find_the_difference("Python", "Pythonn"), "n")
        self.assertEqual(find_the_difference("Case", "CaseS"), "S")


if __name__ == "__main__":
    unittest.main()