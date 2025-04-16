import unittest
from kth_largest_element_in_array import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_small_array(self):
        nums = [3, 2, 1, 5, 6, 4]
        self.assertEqual(self.solution.find_kth_largest(nums, 2), 5)

    def test_large_k(self):
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        self.assertEqual(self.solution.find_kth_largest(nums, 4), 4)

    def test_single_element(self):
        nums = [1]
        self.assertEqual(self.solution.find_kth_largest(nums, 1), 1)

    def test_edge_case(self):
        nums = [2, 1]
        self.assertEqual(self.solution.find_kth_largest(nums, 2), 1)

    def test_special_case(self):
        nums = [1] * 50000
        self.assertEqual(self.solution.find_kth_largest(nums, 50000), 1)

    def test_duplicates(self):
        nums = [3, 1, 2, 4, 2]
        self.assertEqual(self.solution.find_kth_largest(nums, 3), 2)

    def test_sorted_array(self):
        nums = [1, 2, 3, 4, 5, 6]
        self.assertEqual(self.solution.find_kth_largest(nums, 3), 4)


if __name__ == '__main__':
    unittest.main()