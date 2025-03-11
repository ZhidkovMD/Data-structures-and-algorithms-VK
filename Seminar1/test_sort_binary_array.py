import unittest
from sort_binary_array import sort_binary_array


class TestSortBinaryArray(unittest.TestCase):
    def test_example_1(self):
        nums = [1, 0, 1, 0, 1, 0]
        sort_binary_array(nums)
        self.assertEqual(nums, [0, 0, 0, 1, 1, 1])

    def test_example_2(self):
        nums = [1, 1, 1, 1, 0, 0, 0, 0]
        sort_binary_array(nums)
        self.assertEqual(nums, [0, 0, 0, 0, 1, 1, 1, 1])

    def test_example_3(self):
        nums = [0, 0, 0, 0]
        sort_binary_array(nums)
        self.assertEqual(nums, [0, 0, 0, 0])

    def test_example_4(self):
        nums = [1, 1, 1, 1]
        sort_binary_array(nums)
        self.assertEqual(nums, [1, 1, 1, 1])

    def test_example_5(self):
        nums = [0, 1, 0, 1, 0, 1]
        sort_binary_array(nums)
        self.assertEqual(nums, [0, 0, 0, 1, 1, 1])

    def test_example_6(self):
        nums = [1, 0]
        sort_binary_array(nums)
        self.assertEqual(nums, [0, 1])

    def test_example_7(self):
        nums = [0, 1]
        sort_binary_array(nums)
        self.assertEqual(nums, [0, 1])

    def test_empty_list(self):
        nums = []
        sort_binary_array(nums)
        self.assertEqual(nums, [])


if __name__ == '__main__':
    unittest.main()