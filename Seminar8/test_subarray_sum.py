import unittest
from subarray_sum import Solution

class TestSubarraySum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_array(self):
        self.assertEqual(self.solution.subarray_sum([], 5), 0)

    def test_single_element_match(self):
        self.assertEqual(self.solution.subarray_sum([5], 5), 1)

    def test_single_element_no_match(self):
        self.assertEqual(self.solution.subarray_sum([3], 5), 0)

    def test_subarray_cases(self):
        test_cases = [
            ([1, 1, 1], 2, 2),
            ([1, 2, 3], 3, 2),
            ([1, -1, 0], 0, 3),
            ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
            ([0, 0, 0, 0, 0], 0, 15),
        ]
        
        for nums, k, expected in test_cases:
            with self.subTest(nums=nums, k=k):
                self.assertEqual(self.solution.subarray_sum(nums, k), expected)

    def test_large_array(self):
        nums = [1] * 1000
        k = 100
        self.assertEqual(self.solution.subarray_sum(nums, k), 901)

    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        k = -9
        self.assertEqual(self.solution.subarray_sum(nums, k), 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)