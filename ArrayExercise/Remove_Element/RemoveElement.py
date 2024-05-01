from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = nums.count(val)
        while counter > 0:
            for n in nums:
                if n == val:
                    nums.remove(n)
                    counter -= 1
        return len(nums)

    def removeElement2(self, nums: List[int], val: int) -> int:
        r = 0
        while r < len(nums):
            if nums[r] == val:
                nums.remove(nums[r])
                r = 0
            else:
                r += 1

        return len(nums)
