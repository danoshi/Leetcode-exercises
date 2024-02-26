from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeroes = arr.count(0)
        length = len(arr)
        for i in range(length-1, -1, -1):
            if i + zeroes < length:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0:
                zeroes -= 1
                if i + zeroes < length:
                    arr[i + zeroes] = 0


test = Solution()
print(test.duplicateZeros([1,0,2,3,0,4,5,0]))