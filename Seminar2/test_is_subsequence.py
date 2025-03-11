import unittest
from is_subsequence import Solution1, Solution2, Solution3


class TestIsSubsequence(unittest.TestCase):
    def _test_solution(self, solution):
        self.assertTrue(solution.is_subsequence("abc", "ahbgdc"))
        self.assertFalse(solution.is_subsequence("axc", "ahbgdc"))
        self.assertTrue(solution.is_subsequence("", "ahbgdc"))
        self.assertTrue(solution.is_subsequence("bdc", "ahbgdc"))
        self.assertFalse(solution.is_subsequence("abc", "acb"))
        self.assertTrue(solution.is_subsequence("abc", "abc"))
        self.assertFalse(solution.is_subsequence("abc", "ab"))
        self.assertTrue(solution.is_subsequence("a", "a"))

    def test_solution1(self):
        solution = Solution1()
        self._test_solution(solution)

    def test_solution2(self):
        solution = Solution2()
        self._test_solution(solution)

    def test_solution3(self):
        solution = Solution3()
        self._test_solution(solution)


if __name__ == "__main__":
    unittest.main()