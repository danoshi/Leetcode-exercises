import math
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        digits = 0
        counter = 0
        for x in nums:
            while x > 0:
                x = math.floor(x / 10)
                digits += 1
            if digits % 2 == 0:
                counter += 1
            digits = 0
        return counter




test = Solution()
print(test.findNumbers([555,901,482,1771]))