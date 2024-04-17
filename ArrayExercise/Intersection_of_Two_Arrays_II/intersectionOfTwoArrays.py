from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        final_arr = []

        for i in nums1:
            for n in nums2:
                if i == n:
                    final_arr.append(n)
                    nums2.remove(n)
                    break
        return final_arr
