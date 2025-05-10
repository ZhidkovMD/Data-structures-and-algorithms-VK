import unittest
from longest_palindrome import Solution


class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        self.assertEqual(self.solution.longest_palindrome(""), "")

    def test_single_character(self):
        self.assertEqual(self.solution.longest_palindrome("a"), "a")

    def test_all_identical_characters(self):
        self.assertEqual(self.solution.longest_palindrome("bbb"), "bbb")

    def test_typical_cases(self):
        test_cases = [
            ("babad", ["bab", "aba"]),
            ("cbbd", "bb"),
            ("racecar", "racecar"),
            ("abacdfgdcaba", "aba"),
            ("aacabdkacaa", "aca"),
            ("abcde", "a"),
            ("aaabaaaa", "aaabaaa")
        ]

        for input_str, expected in test_cases:
            with self.subTest(input=input_str, expected=expected):
                result = self.solution.longest_palindrome(input_str)
                if isinstance(expected, list):
                    self.assertIn(result, expected)
                else:
                    self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main(verbosity=2)