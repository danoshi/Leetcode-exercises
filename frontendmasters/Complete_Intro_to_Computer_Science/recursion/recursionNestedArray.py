from typing import List


class Solution:
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


test = Solution()
test.recursionNestedArray([10, 5, 3, 8, 2, 6, 4, 7, 9, 1])
print(test.recursionNestedArray([1, [2], 3]))
