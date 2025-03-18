from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """_summary_

        Args:
            nums (List[int]): _description_

        Returns:
            List[int]: _description_
        """
        arr = []
        for x in nums:
            arr.append(x * x)
        arr.sort()
        return arr
