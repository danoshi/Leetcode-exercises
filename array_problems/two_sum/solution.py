from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two numbers in the array that add up to target.

        Args:
            nums: List of integers
            target: Target sum

        Returns:
            List containing indices of the two numbers

        Time complexity: O(n)
        Space complexity: O(n)
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
