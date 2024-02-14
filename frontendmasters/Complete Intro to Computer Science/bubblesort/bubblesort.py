from typing import List


class Solution:
    def bubbleSort(self, nums: List[int]) -> int:
        count = 1
        a = len(nums)
        while count != a:  # run until my sorting is done
            for i in range(0, a - 1):  
                if nums[i] > nums[i + 1]:  # if my current num is bigger then the next
                    temp: int = nums[i]  # if yes save the current into a temp
                    nums[i] = nums[i + 1]  # set the current to the next since its smaller
                    nums[i + 1] = temp  # set the higher element one index ahead
            count += 1
        print(nums)


test = Solution()
test.bubbleSort([10, 5, 3, 8, 2, 6, 4, 7, 9, 1])
test.bubbleSort([10, 5, 3, 8])
test.bubbleSort([2, 1])
test.bubbleSort([2])
