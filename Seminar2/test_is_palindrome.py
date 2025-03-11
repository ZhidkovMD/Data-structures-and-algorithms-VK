import unittest
from is_palindrome import Solution1, Solution2


class TestIsPalindrome(unittest.TestCase):
    def _test_solution(self, solution):
        self.assertTrue(solution.is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(solution.is_palindrome("race a car"))
        self.assertTrue(solution.is_palindrome(" "))
        self.assertTrue(solution.is_palindrome("Madam"))
        self.assertFalse(solution.is_palindrome("hello world"))
        self.assertTrue(solution.is_palindrome("12321"))
        self.assertFalse(solution.is_palindrome("123abc"))
        self.assertTrue(solution.is_palindrome("No lemon, no melon"))

    def test_solution1(self):
        solution = Solution1()
        self._test_solution(solution)

    def test_solution2(self):
        solution = Solution2()
        self._test_solution(solution)


if __name__ == "__main__":
    unittest.main()