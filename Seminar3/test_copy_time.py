import unittest
from copy_time import very_easy_task


class TestMinTimeToCopy(unittest.TestCase):
    def test_zero_copies(self):
        self.assertEqual(very_easy_task(0, 1, 1), 0)

    def test_one_copy_fast_first(self):
        self.assertEqual(very_easy_task(1, 1, 10), 1)

    def test_one_copy_fast_second(self):
        self.assertEqual(very_easy_task(1, 10, 1), 1)

    def test_two_copies_equal_speed(self):
        self.assertEqual(very_easy_task(2, 1, 1), 2)

    def test_two_copies_different_speed(self):
        self.assertEqual(very_easy_task(2, 1, 10), 2)

    def test_three_copies_equal_speed(self):
        self.assertEqual(very_easy_task(3, 1, 1), 2)

    def test_three_copies_different_speed(self):
        self.assertEqual(very_easy_task(3, 1, 10), 3)

    def test_large_n_equal_speed(self):
        self.assertEqual(very_easy_task(100, 1, 1), 51)

    def test_large_n_different_speed(self):
        self.assertEqual(very_easy_task(5, 3, 5), 12)

    def test_large_n_one_very_fast(self):
        self.assertEqual(very_easy_task(100, 1, 100), 100)


if __name__ == '__main__':
    unittest.main()