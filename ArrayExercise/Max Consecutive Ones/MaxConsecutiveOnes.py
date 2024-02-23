from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        arr = []
        counter = 0
        for i in nums:
            if i == 1:
                counter += 1
            elif i != 1:
                arr.append(counter)
                counter = 0
            arr.append(counter)
        arr.sort()
        return arr[len(arr) - 1]


test = Solution()
print(test.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))