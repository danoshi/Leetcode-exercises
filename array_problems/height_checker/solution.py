from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """_summary_

        Args:
            heights (List[int]): _description_

        Returns:
            int: _description_
        """
        start = 0
        counter = 0
        sorting = heights.copy()
        sorting.sort()
        while start < len(heights):
            if sorting[start] != heights[start]:
                counter += 1
            start += 1
        return counter
