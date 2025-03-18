from typing import List
from math import floor, sqrt


class Solution:
    def two_crystal_balls(self, breaks: List[bool]) -> int:
        """_summary_

        Args:
            breaks (List[bool]): _description_

        Returns:
            int: _description_
        """
        n = len(breaks)
        jmpAmount = floor(sqrt(n))

        i = jmpAmount
        while i < n and not breaks[i]:
            i += jmpAmount

        if i >= n:
            return -1

        i -= jmpAmount

        for j in range(jmpAmount):
            if i >= n:
                return -1
            if breaks[i]:
                return i + 1
            i += 1

        return -1


solution = Solution()

res = solution.two_crystal_balls([False, False, False, True, True, True])
print(res)
