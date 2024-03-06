import math
from typing import List


class Solution:
    def quickSort(self, nums: List[int]):
        length = len(nums)
        # base case if len of array is 0 or 1 return
        if length < 2:
            return nums
        # choose pivot which is last item in an array
        pivot = nums[length - 1]
        # create left and right array
        left = []
        right = []

        for a in range(0, len(nums) - 1):
            # if nums is smaller than pivot append to left
            if nums[a] < pivot:
                left.append(nums[a])
            else:
                # else nums is larger than pivot append to right
                right.append(nums[a])
        # call quicksort on right and left
        l = self.quickSort(left)
        r = self.quickSort(right)
        # append pivot which is a number
        l.append(pivot)
        # extend array l with r
        l.extend(r)
        return l


test = Solution()
print(test.quickSort([10, 5, 3, 8, 2, 6, 4, 7, 9, 1]))
