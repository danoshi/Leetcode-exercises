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
