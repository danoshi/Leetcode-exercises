from typing import List


class Solution:
    def maxProfitA(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        for p in range(1, n):
            if prices[p] > prices[p - 1]:
                profit += prices[p] - prices[p - 1]
        return profit
