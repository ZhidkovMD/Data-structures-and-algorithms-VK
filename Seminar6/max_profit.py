from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
            
        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1
            
        return max_profit