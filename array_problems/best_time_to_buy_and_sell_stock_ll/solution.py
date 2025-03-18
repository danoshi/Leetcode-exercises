from typing import List


class Solution:
    def maxProfitA(self, prices: List[int]) -> int:
        """_summary_

        Args:
            prices (List[int]): _description_

        Returns:
            int: _description_
        """
        profit = 0
        n = len(prices)
        for p in range(1, n):
            if prices[p] > prices[p - 1]:
                profit += prices[p] - prices[p - 1]
        return profit
