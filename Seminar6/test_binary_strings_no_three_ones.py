import unittest
from binary_strings_no_three_ones import count_binary_strings_no_three_ones

class TestBinaryStringsNoThreeOnes(unittest.TestCase):
    def test_zero_length(self):
        self.assertEqual(count_binary_strings_no_three_ones(0), 0)

    def test_single_length(self):
        self.assertEqual(count_binary_strings_no_three_ones(1), 2)

    def test_double_length(self):
        self.assertEqual(count_binary_strings_no_three_ones(2), 4)

    def test_typical_cases(self):
        test_cases = [
            (3, 7),
            (4, 13),
            (5, 24),
        ]
        for n, expected in test_cases:
            with self.subTest(n=n, expected=expected):
                self.assertEqual(count_binary_strings_no_three_ones(n), expected)

    def test_large_input(self):
        self.assertEqual(count_binary_strings_no_three_ones(10), 504)

if __name__ == '__main__':
    unittest.main()