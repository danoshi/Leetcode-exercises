from math import floor
from typing import List


class Solution:
    def linearSearch(self, id, array):
        """_summary_

        Args:
            id (_type_): _description_
            array (_type_): _description_

        Returns:
            _type_: _description_
        """
        for n in range(0, len(array)):
            if id == array[n]["id"]:
                return array[n]
        return None

    def binarySearch(self, id, array):
        """_summary_

        Args:
            id (_type_): _description_
            array (_type_): _description_

        Returns:
            _type_: _description_
        """
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

    def binary_search_primeagen(self, nums: List[int], num: int) -> bool:
        """_summary_

        Args:
            nums (List[int]): _description_
            num (int): _description_

        Returns:
            bool: _description_
        """
        lowest_value = 0
        highest_value = len(nums) - 1

        while lowest_value <= highest_value:
            mid_value = floor((lowest_value + highest_value) / 2)
            value = nums[mid_value]
            if value == num:
                return True
            elif value > num:
                highest_value = mid_value - 1
            else:
                lowest_value = mid_value + 1
        return False
