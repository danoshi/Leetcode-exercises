from typing import List


class Solution:
    def maxProfitA(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)
        for p in range(1, n):
            if prices[p] > prices[p-1]:
                profit += prices[p] - prices[p-1]
        print(profit)

test = Solution()
test.maxProfitA([1,2,3,4,5]) # 4
test.maxProfitA([7,1,5,3,6,4]) # 7
test.maxProfitA([7,6,4,3,1]) # 0
test.maxProfitA([7,1,5,3,6,4]) # 7
