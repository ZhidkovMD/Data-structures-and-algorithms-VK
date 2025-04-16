import unittest
from check_heap import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_heap(self):
        self.assertTrue(self.solution.is_heap([]))

    def test_single_element(self):
        self.assertTrue(self.solution.is_heap([1]))

    def test_valid_min_heap(self):
        self.assertTrue(self.solution.is_heap([1, 2, 3, 4, 5, 6]))

    def test_valid_max_heap(self):
        self.assertTrue(self.solution.is_heap([6, 4, 5, 1, 2, 3]))

    def test_not_a_heap(self):
        self.assertFalse(self.solution.is_heap([1, 5, 2, 7, 3, 6]))

    def test_partial_heap(self):
        self.assertFalse(self.solution.is_heap([1, 2, 3, 4, 1, 5]))

    def test_large_min_heap(self):
        heap = [0, 2, 1, 4, 3, 8, 5, 6, 7, 9]
        self.assertTrue(self.solution.is_heap(heap))

    def test_large_max_heap(self):
        heap = [9, 7, 8, 5, 6, 3, 4, 1, 2, 0]
        self.assertTrue(self.solution.is_heap(heap))

    def test_mixed_properties(self):
        self.assertFalse(self.solution.is_heap([1, 3, 2, 6, 4, 0]))


if __name__ == '__main__':
    unittest.main()