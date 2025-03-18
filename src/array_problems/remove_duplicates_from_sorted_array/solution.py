from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """_summary_

        Args:
            nums (List[int]): _description_

        Returns:
            int: _description_
        """
        lastvalue = None
        helper = []
        for n in range(1, len(nums)):
            if nums[n] == lastvalue or nums[0] == nums[n]:
                helper.append(nums[n])
            lastvalue = nums[n]
        for h in helper:
            nums.remove(h)
        return len(nums)

    def removeDuplicates2(self, nums: List[int]) -> int:
        """_summary_

        Args:
            nums (List[int]): _description_

        Returns:
            int: _description_
        """
        size = len(nums)
        insertIndex = 1
        for i in range(1, size):
            # Found unique element
            if nums[i - 1] != nums[i]:
                # Updating insertIndex in our main array
                nums[insertIndex] = nums[i]
                # Incrementing insertIndex count by 1
                insertIndex = insertIndex + 1
        return insertIndex
