import unittest
from typing import List
from max_length_balanced_subarray import Solution

class TestMaxLengthBalancedSubarray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_array(self):
        self.assertEqual(self.solution.find_max_length([]), 0)

    def test_single_element(self):
        self.assertEqual(self.solution.find_max_length([0]), 0)
        self.assertEqual(self.solution.find_max_length([1]), 0)

    def test_all_zeros_or_ones(self):
        self.assertEqual(self.solution.find_max_length([0, 0, 0]), 0)
        self.assertEqual(self.solution.find_max_length([1, 1, 1]), 0)

    def test_balanced_subarrays(self):
        test_cases = [
            ([0, 1], 2),
            ([0, 1, 0], 2),
            ([0, 1, 0, 1], 4),
            ([0, 0, 1, 0, 0, 0, 1, 1], 6),
            ([1, 0, 1, 1, 0, 0, 1, 0], 8),
            ([0, 0, 1, 1, 0, 1, 1, 1, 0], 6),
        ]
        
        for nums, expected in test_cases:
            with self.subTest(nums=nums):
                self.assertEqual(self.solution.find_max_length(nums), expected)

    def test_large_arrays(self):
        large_alternating = [0, 1] * 10000
        self.assertEqual(self.solution.find_max_length(large_alternating), 20000)
        
        large_with_balance = [0] * 10000 + [1] * 10000
        self.assertEqual(self.solution.find_max_length(large_with_balance), 20000)
        
        large_no_balance = [0] * 100000
        self.assertEqual(self.solution.find_max_length(large_no_balance), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)