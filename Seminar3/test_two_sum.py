import unittest
from two_sum import two_sum


class TestTwoSum(unittest.TestCase):
    def test_basic_case(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(two_sum(nums, target), [0, 1])

    def test_no_solution(self):
        nums = [1, 2, 3]
        target = 7
        self.assertIsNone(two_sum(nums, target))

    def test_negative_numbers(self):
        nums = [-3, 4, 3, 90]
        target = 0
        self.assertEqual(two_sum(nums, target), [0, 2])

    def test_duplicate_numbers(self):
        nums = [3, 3]
        target = 6
        self.assertEqual(two_sum(nums, target), [0, 1])

    def test_large_numbers(self):
        nums = [1000000, 500000, 500000]
        target = 1000000
        self.assertEqual(two_sum(nums, target), [1, 2])


if __name__ == '__main__':
    unittest.main()