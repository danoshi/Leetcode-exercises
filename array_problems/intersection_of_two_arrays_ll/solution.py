from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """_summary_

        Args:
            nums1 (List[int]): _description_
            nums2 (List[int]): _description_

        Returns:
            List[int]: _description_
        """
        final_arr = []

        for i in nums1:
            for n in nums2:
                if i == n:
                    final_arr.append(n)
                    nums2.remove(n)
                    break
        return final_arr
