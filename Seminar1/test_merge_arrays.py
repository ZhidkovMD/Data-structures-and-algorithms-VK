import unittest
from merge_arrays import merge_sorted_arrays


class TestMergeSortedArrays(unittest.TestCase):
    def test_example_1(self):
        nums1 = [1, 3, 5]
        nums2 = [2, 4, 6]
        result = merge_sorted_arrays(nums1, nums2)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_example_2(self):
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]
        result = merge_sorted_arrays(nums1, nums2)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_example_3(self):
        nums1 = []
        nums2 = [1, 2, 3]
        result = merge_sorted_arrays(nums1, nums2)
        self.assertEqual(result, [1, 2, 3])

    def test_example_4(self):
        nums1 = [1, 2, 3]
        nums2 = []
        result = merge_sorted_arrays(nums1, nums2)
        self.assertEqual(result, [1, 2, 3])

    def test_example_5(self):
        nums1 = [1, 1, 1]
        nums2 = [2, 2, 2]
        result = merge_sorted_arrays(nums1, nums2)
        self.assertEqual(result, [1, 1, 1, 2, 2, 2])

    def test_example_6(self):
        nums1 = [1, 3, 5, 7]
        nums2 = [2, 4, 6, 8, 10]
        result = merge_sorted_arrays(nums1, nums2)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 10])

    def test_example_7(self):
        nums1 = [-5, 0, 5]
        nums2 = [-10, 10]
        result = merge_sorted_arrays(nums1, nums2)
        self.assertEqual(result, [-10, -5, 0, 5, 10])


if __name__ == '__main__':
    unittest.main()