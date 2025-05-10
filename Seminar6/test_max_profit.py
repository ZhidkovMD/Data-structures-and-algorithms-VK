import unittest
from max_profit import Solution


class TestMaxProfit(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertEqual(self.solution.max_profit([]), 0)

    def test_single_price(self):
        self.assertEqual(self.solution.max_profit([7]), 0)

    def test_no_profit_possible(self):
        self.assertEqual(self.solution.max_profit([7, 6, 5, 4]), 0)

    def test_profit_cases(self):
        test_cases = [
            ([7, 1, 5, 3, 6, 4], 5),
            ([1, 2, 3, 4, 5], 4),
            ([3, 3, 3, 3, 3], 0),
            ([2, 4, 1], 2),
        ]
        
        for prices, expected in test_cases:
            with self.subTest(prices=prices):
                self.assertEqual(self.solution.max_profit(prices), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)