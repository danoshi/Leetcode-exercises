from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        for x in nums:
            arr.append(x * x)
        arr.sort()
        return arr


test = Solution()
print(test.sortedSquares([-4, -1, 0, 3, 10]))
