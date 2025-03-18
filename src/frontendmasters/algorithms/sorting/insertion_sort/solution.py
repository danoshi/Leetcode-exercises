from typing import List


class Solution:
    def insertion_sort(self, nums: List[int]) -> List[int]:
        """_summary_

        Args:
            nums (List[int]): _description_

        Returns:
            List[int]: _description_
        """
        a = len(nums)
        # start the loop at index 1 since we compare the item before with the current one
        for i in range(1, a):
            # assign a var the current value
            numberToInsert = nums[i]
            # previous value in tha arr
            j = i - 1
            # sort the arr until previous value is bigger than the current and j is greater/equal 0
            while nums[j] > numberToInsert and j >= 0:
                # when the condition is met previous is now the current value
                nums[j + 1] = nums[j]
                # j starts again to be the previous value
                j -= 1
            # the current value is now the number which is being switched
            nums[j + 1] = numberToInsert
        return nums
