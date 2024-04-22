from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums) - 1
        count = 0
        if length < 1:
            return
        should_restart = True
        while should_restart:
            should_restart = False
            for n in nums:
                if n == 0:
                    nums.remove(n)
                    count += 1
                    should_restart = True
        while count > 0:
            nums.append(0)
            count -= 1

    def moveZeroes2(self, nums: List[int]) -> None:
        l = 0
        r = 0
        while r < len(nums):
            if nums[r] != 0:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
            r += 1
