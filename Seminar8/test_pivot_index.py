import unittest
from pivot_index import Solution

class TestPivotIndex(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_array(self):
        self.assertEqual(self.solution.pivot_index([]), -1)

    def test_single_element(self):
        self.assertEqual(self.solution.pivot_index([5]), 0)

    def test_no_pivot(self):
        self.assertEqual(self.solution.pivot_index([1, 2, 3]), -1)

    def test_pivot_cases(self):
        test_cases = [
            ([1, 7, 3, 6, 5, 6], 3),
            ([1, 2, 3, 4, 5, 6], -1),
            ([2, 1, -1], 0),
            ([1, -1, 2], 2),
            ([0, 0, 0, 0], 0),
            ([-1, -1, -1, 0, 1, 1], 0),
        ]
        
        for nums, expected in test_cases:
            with self.subTest(nums=nums):
                self.assertEqual(self.solution.pivot_index(nums), expected)

    def test_large_array(self):
        nums = [1] * 10000 + [10000] + [1] * 10000
        self.assertEqual(self.solution.pivot_index(nums), 10000)
        
        nums = [0] * 100000
        self.assertEqual(self.solution.pivot_index(nums), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)