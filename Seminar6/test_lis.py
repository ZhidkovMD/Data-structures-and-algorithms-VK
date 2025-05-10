import unittest
from lis import Solution


class TestLengthOfLIS(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertEqual(self.solution.length_of_lis([]), 0)

    def test_single_element(self):
        self.assertEqual(self.solution.length_of_lis([5]), 1)

    def test_all_equal_elements(self):
        self.assertEqual(self.solution.length_of_lis([2, 2, 2]), 1)

    def test_typical_cases(self):
        test_cases = [
            ([1, 2, 3, 4], 4),
            ([4, 3, 2, 1], 1),
            ([10, 9, 2, 5, 3, 7, 101, 18], 4),
            ([0, 8, 4, 12, 2, 10], 3),
            ([1, 3, 6, 7, 9, 4, 10, 5, 6], 6)
        ]
        
        for nums, expected in test_cases:
            with self.subTest(nums=nums, expected=expected):
                self.assertEqual(self.solution.length_of_lis(nums), expected)

    def test_large_inputs(self):
        large_test_cases = [
            (list(range(1000)), 1000),
            (list(range(1000, 0, -1)), 1),
            ([1] * 1000, 1)
        ]
        
        for nums, expected in large_test_cases:
            with self.subTest(nums=f"len={len(nums)}", expected=expected):
                self.assertEqual(self.solution.length_of_lis(nums), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)