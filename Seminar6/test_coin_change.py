import unittest
from typing import List
from coin_change import Solution


class TestCoinChange(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_zero_amount(self):
        self.assertEqual(self.solution.coin_change([1, 2, 5], 0), 0)

    def test_no_coins(self):
        self.assertEqual(self.solution.coin_change([], 5), -1)

    def test_impossible_amount(self):
        self.assertEqual(self.solution.coin_change([2], 3), -1)

    def test_typical_cases(self):
        test_cases = [
            (([1, 2, 5], 11), 3),
            (([2], 4), 2),
            (([1, 3, 4], 6), 2),
            (([186, 419, 83, 408], 6249), 20),
        ]

        for (coins, amount), expected in test_cases:
            with self.subTest(coins=coins, amount=amount):
                self.assertEqual(
                    self.solution.coin_change(coins, amount),
                    expected
                )

    def test_large_amount(self):
        coins = [1, 2, 5, 10, 20, 50]
        amount = 10000
        result = self.solution.coin_change(coins, amount)
        self.assertEqual(result, 200)


if __name__ == "__main__":
    unittest.main(verbosity=2)