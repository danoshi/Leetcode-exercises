import math
from typing import List


class Solution:
    def getDigit(self, number, place, longestNum):
        chars = str(number)
        size = len(chars)
        mod = longestNum - size
        index = place - mod
        if 0 <= index < size:
            return chars[index]
        else:
            return 0

    def getLongestNumber(self, arr):
        longest = 0
        for i in range(0, len(arr)):
            currentlen = len(str(arr[i]))
            if currentlen > longest:
                longest = currentlen
        return longest


    def radixSort(self, array):
        longestnum = self.getLongestNumber(array)

        buckets = []
        for _ in range(10):
            buckets.append([])

        for i in range(longestnum - 1, -1, -1):
            while len(array):
                current = array.pop(0)
                buckets[int(self.getDigit(current, i, longestnum))].append(current)
            for j in range(0, 10):
                while len(buckets[j]):
                    array.append(buckets[j].pop(0))

        return array



test = Solution()
print(test.getDigit(1391, 0, 4))
print(test.getLongestNumber([1,10,100,1000]))
print(test.radixSort([2, 20324, 2323,3,434, 23,1]))
