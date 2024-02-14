from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastvalue = None
        helper = []
        for n in range(1, len(nums)):
            if nums[n] == lastvalue or nums[0] == nums[n]:
                helper.append(nums[n])
            lastvalue = nums[n]
        for h in helper:
            nums.remove(h)
        return len(nums)

test = Solution()
test.removeDuplicates([1,1,2])
