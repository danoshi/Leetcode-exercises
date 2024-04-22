from collections import Counter
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        counter = 0
        length = len(arr)
        count = Counter(arr)
        if count[0] >= 2:
            return True
        while counter < length:
            for n in arr:
                erg = arr[counter] * 2
                if n == erg and n != 0:
                    return True
            counter += 1
        return False
