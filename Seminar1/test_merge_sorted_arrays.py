import unittest
from merge_sorted_arrays import merge


class TestMergeSortedArrays(unittest.TestCase):
    def test_example_1(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

    def test_example_2(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])

    def test_example_3(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1])

    def test_all_elements_in_nums2(self):
        nums1 = [4, 5, 6, 0, 0, 0]
        m = 3
        nums2 = [1, 2, 3]
        n = 3
        merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

    def test_empty_nums1(self):
        nums1 = [0, 0, 0]
        m = 0
        nums2 = [1, 2, 3]
        n = 3
        merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3])

    def test_empty_nums2(self):
        nums1 = [1, 2, 3]
        m = 3
        nums2 = []
        n = 0
        merge(nums1, m, nums2, n)
        self.assertEqual(nums1, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()