from typing import List


class Solution:
    def bubble_sort(self, nums: List[int]) -> List[int]:
        """_summary_

        Args:
            nums (List[int]): _description_

        Returns:
            List[int]: _description_
        """
        count = 1
        a = len(nums)
        while count != a:  # run until my sorting is done
            for i in range(0, a - 1):
                if nums[i] > nums[i + 1]:  # if my current num is bigger then the next
                    temp: int = nums[i]  # if yes save the current into a temp
                    nums[i] = nums[
                        i + 1
                    ]  # set the current to the next since its smaller
                    nums[i + 1] = temp  # set the higher element one index ahead
            count += 1
        return nums
