from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        r = 0
        while r < len(nums):
            if nums[r] % 2 == 0:
                # swap the elements with each other
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        return nums
