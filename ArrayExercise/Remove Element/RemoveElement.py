from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = nums.count(val)
        while counter > 0:
            for n in nums:
                if n == val:
                    nums.remove(n)
                    counter -=1
        return len(nums)



test = Solution()
print(test.removeElement([0,1,2,2,3,0,4,2], 2))
