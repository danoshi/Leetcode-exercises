import math
from typing import List


class Solution:
    def mergeSort(self, nums: List[int]):
        # base case, return arr if len is 1 or 0
        length: int = len(nums)
        if length < 2:
            return nums
        # break into smaller arrays
        middle: int = math.floor(length / 2)
        # left side of array (python slicing)
        left = nums[0:middle]
        # right side of array
        right = nums[middle:]

        # call mergesort on the array to get arr with len 1
        sortedLeft = self.mergeSort(left)
        sortedRight = self.mergeSort(right)

        # return the merge of left and right
        return self.merge(sortedLeft, sortedRight)

    def merge(self, leftarr, rightarr):
        result = []
        # compare so long after nothing is in the array
        while len(leftarr) and len(rightarr):
            # check if left is smaller or equal than right item
            if leftarr[0] <= rightarr[0]:
                # if yes append left array first item and delete it
                result.append(leftarr.pop(0))
            else:
                # if not append right array first item and delete it
                result.append(rightarr.pop(0))
        # append left side arr to result
        result.extend(leftarr)
        # append right side arr to result
        result.extend(rightarr)
        return result


test = Solution()
print(test.mergeSort([10, 5, 3, 8, 2, 6, 4, 7, 9, 1]))
print(test.mergeSort([10, 5, 3, 8]))
print(test.mergeSort([2, 1]))
print(test.mergeSort([2]))

