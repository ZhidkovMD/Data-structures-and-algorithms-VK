import unittest
from sqrt import my_sqrt


class TestMySqrt(unittest.TestCase):
    def test_perfect_squares(self):
        self.assertEqual(my_sqrt(1), 1)
        self.assertEqual(my_sqrt(4), 2)
        self.assertEqual(my_sqrt(9), 3)
        self.assertEqual(my_sqrt(16), 4)
        self.assertEqual(my_sqrt(25), 5)

    def test_non_perfect_squares(self):
        self.assertEqual(my_sqrt(2), 1)
        self.assertEqual(my_sqrt(3), 1)
        self.assertEqual(my_sqrt(5), 2)
        self.assertEqual(my_sqrt(10), 3)
        self.assertEqual(my_sqrt(15), 3)
        self.assertEqual(my_sqrt(24), 4)

    def test_edge_cases(self):
        self.assertEqual(my_sqrt(0), 0)
        self.assertEqual(my_sqrt(2147395599), 46339)
        self.assertEqual(my_sqrt(2147483647), 46340)


if __name__ == '__main__':
    unittest.main()