# test_reverse_array.py

import unittest
from reverse_array import reverse_array


class TestReverseArray(unittest.TestCase):
    def test_example_1(self):
        nums = [1, 2, 3, 4, 5]
        reverse_array(nums)
        self.assertEqual(nums, [5, 4, 3, 2, 1])

    def test_example_2(self):
        nums = [10, 20, 30, 40]
        reverse_array(nums)
        self.assertEqual(nums, [40, 30, 20, 10])

    def test_empty_list(self):
        nums = []
        reverse_array(nums)
        self.assertEqual(nums, [])

    def test_single_element(self):
        nums = [42]
        reverse_array(nums)
        self.assertEqual(nums, [42])

    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4]
        reverse_array(nums)
        self.assertEqual(nums, [-4, -3, -2, -1])

    def test_mixed_numbers(self):
        nums = [0, -1, 2, -3, 4]
        reverse_array(nums)
        self.assertEqual(nums, [4, -3, 2, -1, 0])


if __name__ == '__main__':
    unittest.main()