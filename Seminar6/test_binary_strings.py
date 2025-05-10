import unittest
from binary_strings import count_binary_strings

class TestBinaryStrings(unittest.TestCase):
    def test_zero_length(self):
        self.assertEqual(count_binary_strings(0), 0)

    def test_single_length(self):
        self.assertEqual(count_binary_strings(1), 2)

    def test_typical_cases(self):
        test_cases = [
            (2, 3),
            (3, 5),
            (4, 8),
            (5, 13),
            (6, 21),
        ]
        for n, expected in test_cases:
            with self.subTest(n=n, expected=expected):
                self.assertEqual(count_binary_strings(n), expected)

    def test_large_input(self):
        self.assertEqual(count_binary_strings(20), 17711)

if __name__ == '__main__':
    unittest.main()