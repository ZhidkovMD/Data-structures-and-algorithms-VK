import unittest
from rotate_array import rotate1, rotate2


class TestRotateArray(unittest.TestCase):
    def test_rotate1_example_1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        rotate1(nums, k)
        self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

    def test_rotate1_example_2(self):
        nums = [-1, -100, 3, 99]
        k = 2
        rotate1(nums, k)
        self.assertEqual(nums, [3, 99, -1, -100])

    def test_rotate1_k_greater_than_length(self):
        nums = [1, 2, 3]
        k = 5
        rotate1(nums, k)
        self.assertEqual(nums, [2, 3, 1])

    def test_rotate2_example_1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        rotate2(nums, k)
        self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

    def test_rotate2_example_2(self):
        nums = [-1, -100, 3, 99]
        k = 2
        rotate2(nums, k)
        self.assertEqual(nums, [3, 99, -1, -100])

    def test_rotate2_k_greater_than_length(self):
        nums = [1, 2, 3]
        k = 5
        rotate2(nums, k)
        self.assertEqual(nums, [2, 3, 1])


if __name__ == '__main__':
    unittest.main()