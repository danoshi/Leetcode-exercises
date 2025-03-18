from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """_summary_

        Args:
            nums (List[int]): _description_

        Returns:
            bool: _description_
        """
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
        """_summary_

        Args:
            nums (List[int]): _description_

        Returns:
            bool: _description_
        """
        length = len(nums) - 1
        nums.sort()
        print(nums)
        for n in range(0, length):
            if nums[n] == nums[n + 1]:
                return True
        return False
