import math
from typing import List


class Solution:
    def linearSearch(self, id, array):
        for n in range(0, len(array)):
            if id == array[n]["id"]:
                return array[n]
        return None

    def binarySearch(self, id, array):
        # ONLY WORKS FOR SORTED ARRAYS
        minimum = 0
        maximum = len(array) - 1

        while minimum <= maximum:
            index = minimum + maximum // 2

            if array[index]["id"] < id:
                minimum = index + 1
            elif array[index]["id"] > id:
                maximum = index - 1
            else:
                return array[index]


test = Solution()
# print(test.linearSearch(10, [
#     {"id": 1, "name": "Sam"},
#     {"id": 11, "name": "Sarah"},
#     {"id": 21, "name": "John"},
#     {"id": 10, "name": "Burke"},
#     {"id": 14, "name": "Ben"}
# ]))
print(test.binarySearch(10, [
    {"id": 1, "name": "Sam"},
    {"id": 10, "name": "Sarah"},
    {"id": 11, "name": "John"},
    {"id": 21, "name": "Burke"},
    {"id": 22, "name": "Ben"}
]))
