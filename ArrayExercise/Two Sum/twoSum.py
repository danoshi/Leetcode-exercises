from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        length = len(nums) - 1
        k = len(nums) - 1
        while k > 0:
            for n in range(0, length):
                if (nums[k] + nums[n]) == target:
                    arr.append(k)
                    arr.append(n)
                    return arr
            k -= 1

test = Solution()
#print(test.twoSum([2,7,11,15], 9))
print(test.twoSum([3,2,3], 6))

