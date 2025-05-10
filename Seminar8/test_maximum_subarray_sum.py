import unittest
from typing import List
from maximum_subarray_sum import Solution

class TestMaximumSubarraySum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_array(self):
        self.assertEqual(self.solution.maximum_subarray_sum([], 1), 0)
    
    def test_k_greater_than_length(self):
        self.assertEqual(self.solution.maximum_subarray_sum([1, 2, 3], 5), 0)
    
    def test_k_zero(self):
        self.assertEqual(self.solution.maximum_subarray_sum([1, 2, 3], 0), 0)

    def test_subarray_cases(self):
        test_cases = [
            ([1, 2, 3, 4, 5], 2, 9), 
            ([10, 2, -3, 4, 5], 3, 9),
            ([-1, -2, -3, -4], 2, -3),
            ([1, 1, 1, 1, 1], 3, 3),
            ([3, -1, 4, -2, 5], 2, 3),
        ]
        
        for nums, k, expected in test_cases:
            with self.subTest(nums=nums, k=k):
                self.assertEqual(self.solution.maximum_subarray_sum(nums, k), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)