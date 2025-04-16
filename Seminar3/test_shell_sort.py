import unittest
from shell_sort import shell_sort


class TestShellSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(shell_sort([]), [])

    def test_single_element(self):
        self.assertEqual(shell_sort([2025]), [2025])

    def test_sorted_list(self):
        self.assertEqual(shell_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(shell_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_random_order(self):
        self.assertEqual(shell_sort([3, 1, 4, 1, 5, 99, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 99])

    def test_negative_numbers(self):
        self.assertEqual(shell_sort([-3, -1, -2, -4]), [-4, -3, -2, -1])

    def test_duplicates(self):
        self.assertEqual(shell_sort([2, 2, 2, 1, 1, 1]), [1, 1, 1, 2, 2, 2])


if __name__ == '__main__':
    unittest.main()