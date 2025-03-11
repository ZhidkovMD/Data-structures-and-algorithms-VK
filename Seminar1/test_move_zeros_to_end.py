import unittest
from move_zeros_to_end import move_zeros_to_end


class TestMoveZerosToEnd(unittest.TestCase):
    def test_example_1(self):
        nums = [0, 1, 0, 3, 12]
        move_zeros_to_end(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_example_2(self):
        nums = [0, 0, 0, 1, 2, 3]
        move_zeros_to_end(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0, 0])

    def test_example_3(self):
        nums = [1, 2, 3, 0, 0, 0]
        move_zeros_to_end(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0, 0])

    def test_example_4(self):
        nums = [1, 2, 3, 4, 5]
        move_zeros_to_end(nums)
        self.assertEqual(nums, [1, 2, 3, 4, 5])

    def test_example_5(self):
        nums = [0, 0, 0]
        move_zeros_to_end(nums)
        self.assertEqual(nums, [0, 0, 0])

    def test_example_6(self):
        nums = [1, 0, 2, 0, 3, 0]
        move_zeros_to_end(nums)
        self.assertEqual(nums, [1, 2, 3, 0, 0, 0])

    def test_empty_list(self):
        nums = []
        move_zeros_to_end(nums)
        self.assertEqual(nums, [])

    def test_single_element_zero(self):
        nums = [0]
        move_zeros_to_end(nums)
        self.assertEqual(nums, [0])

    def test_single_element_non_zero(self):
        nums = [1]
        move_zeros_to_end(nums)
        self.assertEqual(nums, [1])


if __name__ == '__main__':
    unittest.main()