import unittest
from two_sum import two_sum


class TestTwoSum(unittest.TestCase):
    def test_example_1(self):
        numbers = [2, 7, 11, 15]
        target = 9
        self.assertEqual(two_sum(numbers, target), [1, 2])

    def test_example_2(self):
        numbers = [2, 3, 4]
        target = 6
        self.assertEqual(two_sum(numbers, target), [1, 3])

    def test_example_3(self):
        numbers = [-1, 0]
        target = -1
        self.assertEqual(two_sum(numbers, target), [1, 2])

    def test_no_solution(self):
        numbers = [1, 2, 3, 4]
        target = 10
        self.assertEqual(two_sum(numbers, target), [])

    def test_large_numbers(self):
        numbers = [1000000000, 2000000000, 3000000000]
        target = 5000000000
        self.assertEqual(two_sum(numbers, target), [2, 3])


if __name__ == '__main__':
    unittest.main()