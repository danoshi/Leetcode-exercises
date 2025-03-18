from typing import List


class Solution:
    def linear_search(self, num: int, nums: List[int]) -> int:
        """Linear search algorithm that finds the index of a number in a list.

        Args:
            num (int): The number to search for
            nums (List[int]): The list to search in

        Returns:
            int: The index of the number if found, -1 otherwise
        """
        for i, n in enumerate(nums):
            if n == num:
                return i
        return -1