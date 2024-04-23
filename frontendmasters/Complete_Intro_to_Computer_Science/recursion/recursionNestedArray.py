from typing import List


class SolutionNestedArray:
    def recursionNestedArray(self, nums):
        erg = 0
        for i in range(len(nums)):
            current = nums[i]
            # if current is a nested array call the function again with the array
            if isinstance(current, list):
                erg += self.recursionNestedArray(current)
            # if it's a number just add it to the sum
            else:
                erg += current
        return erg
