import unittest
from move_even_to_front import move_even_to_front


class TestMoveEvenToFront(unittest.TestCase):
    def test_example_1(self):
        nums = [3, 1, 2, 4, 6, 5]
        move_even_to_front(nums)
        self.assertEqual(nums, [2, 4, 6, 1, 3, 5])

    def test_example_2(self):
        nums = [1, 3, 5, 7]
        move_even_to_front(nums)
        self.assertEqual(nums, [1, 3, 5, 7])

    def test_example_3(self):
        nums = [2, 4, 6, 8]
        move_even_to_front(nums)
        self.assertEqual(nums, [2, 4, 6, 8])

    def test_example_4(self):
        nums = [1, 2, 3, 4, 5, 6]
        move_even_to_front(nums)
        self.assertEqual(nums, [2, 4, 6, 1, 5, 3])

    def test_example_5(self):
        nums = [0, 1, 0, 3, 12]
        move_even_to_front(nums)
        self.assertEqual(nums, [0, 0, 12, 3, 1])

    def test_example_6(self):
        nums = [7, 3, 5, 2, 8, 10]
        move_even_to_front(nums)
        self.assertEqual(nums, [2, 8, 10, 7, 3, 5])

    def test_empty_list(self):
        nums = []
        move_even_to_front(nums)
        self.assertEqual(nums, [])

    def test_single_element_even(self):
        nums = [4]
        move_even_to_front(nums)
        self.assertEqual(nums, [4])

    def test_single_element_odd(self):
        nums = [3]
        move_even_to_front(nums)
        self.assertEqual(nums, [3])


if __name__ == '__main__':
    unittest.main()