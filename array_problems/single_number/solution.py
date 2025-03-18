from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """_summary_

        Args:
            nums (List[int]): _description_

        Returns:
            int: _description_
        """
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()
