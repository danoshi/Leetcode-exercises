from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = len(nums) - 1
        counter = len(nums)
        while counter >= 0:
            for i in range(0, a):
                temp = nums[a]
                if temp == nums[i]:
                    return True
            a -= 1
            counter -= 1
        return False

    def containsDuplicate2(self, nums: List[int]) -> bool:
        length = len(nums) - 1
        nums.sort()
        print(nums)
        for n in range(0, length):
            if nums[n] == nums[n + 1]:
                return True
        return False


test = Solution()
# print(test.containsDuplicate2([0,4,5,0,3,6]))
print(test.containsDuplicate2([3, 3]))
