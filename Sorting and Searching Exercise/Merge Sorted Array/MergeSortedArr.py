import math
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr = []
        arr[:] = nums1[:m] + nums2[:n]
        arr.sort()
        nums1[:] = arr
        print(nums1)


test = Solution()
test.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
test.merge([1], 1, [], 0)
test.merge([0], 0, [1], 1)