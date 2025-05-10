import unittest
from typing import List
from pascal_triangle import Solution


class TestPascalTriangle(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_zero_rows(self):
        self.assertEqual(self.solution.generate(0), [])

    def test_single_row(self):
        self.assertEqual(self.solution.generate(1), [[1]])

    def test_two_rows(self):
        self.assertEqual(self.solution.generate(2), [[1], [1, 1]])

    def test_typical_cases(self):
        test_cases = [
            (3, [[1], [1, 1], [1, 2, 1]]),
            (4, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]),
            (5, [
                [1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]
            ]),
        ]
        
        for num_rows, expected in test_cases:
            with self.subTest(num_rows=num_rows):
                self.assertEqual(self.solution.generate(num_rows), expected)

    def test_large_input(self):
        result = self.solution.generate(10)
        self.assertEqual(len(result), 10)
        self.assertEqual(result[-1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1])


if __name__ == "__main__":
    unittest.main(verbosity=2)