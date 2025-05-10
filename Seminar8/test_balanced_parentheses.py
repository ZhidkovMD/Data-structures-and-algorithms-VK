import unittest
from balanced_parentheses import Solution

class TestBalancedParentheses(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        self.assertTrue(self.solution.is_valid_parentheses("", 0))
        self.assertTrue(self.solution.is_valid_parentheses("", 5))

    def test_single_character(self):
        self.assertTrue(self.solution.is_valid_parentheses("(", 1))
        self.assertTrue(self.solution.is_valid_parentheses(")", 1))
        self.assertFalse(self.solution.is_valid_parentheses("(", 0))
        self.assertFalse(self.solution.is_valid_parentheses(")", 0))

    def test_already_balanced(self):
        self.assertTrue(self.solution.is_valid_parentheses("()", 0))
        self.assertTrue(self.solution.is_valid_parentheses("(())", 0))
        self.assertTrue(self.solution.is_valid_parentheses("()()", 0))

    def test_balance_with_deletions(self):
        test_cases = [
            ("(()", 1, True),
            ("())", 1, True),
            ("((())", 1, True),
            ("()()()", 0, True),
            ("(()()", 1, True),
            (")(", 2, True),
            ("((())))", 2, False),
        ]
        
        for s, k, expected in test_cases:
            with self.subTest(s=s, k=k):
                self.assertEqual(self.solution.is_valid_parentheses(s, k), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)