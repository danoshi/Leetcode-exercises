from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arrlen = len(arr) - 1
        rightMax = -1

        # Iteration from the last item to the first
        for i in range(arrlen, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax

        return arr
