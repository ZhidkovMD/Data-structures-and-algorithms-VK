import unittest
from sort_colors import sort_colors


class TestSortColors(unittest.TestCase):
    def test_example_1(self):
        nums = [2, 0, 2, 1, 1, 0]
        sort_colors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    def test_example_2(self):
        nums = [2, 0, 1]
        sort_colors(nums)
        self.assertEqual(nums, [0, 1, 2])

    def test_all_zeros(self):
        nums = [0, 0, 0]
        sort_colors(nums)
        self.assertEqual(nums, [0, 0, 0])

    def test_all_ones(self):
        nums = [1, 1, 1]
        sort_colors(nums)
        self.assertEqual(nums, [1, 1, 1])

    def test_all_twos(self):
        nums = [2, 2, 2]
        sort_colors(nums)
        self.assertEqual(nums, [2, 2, 2])

    def test_mixed(self):
        nums = [1, 2, 0, 1, 2, 0]
        sort_colors(nums)
        self.assertEqual(nums, [0, 0, 1, 1, 2, 2])

    def test_empty_list(self):
        nums = []
        sort_colors(nums)
        self.assertEqual(nums, [])

    def test_single_element(self):
        nums = [1]
        sort_colors(nums)
        self.assertEqual(nums, [1])


if __name__ == '__main__':
    unittest.main()