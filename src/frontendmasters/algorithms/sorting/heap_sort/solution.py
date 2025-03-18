from math import floor


class Solution:
    def heapSort(self, array):
        """_summary_

        Args:
            array (_type_): _description_

        Returns:
            _type_: _description_
        """
        self.createMaxHeap(array)
        if array:
            for i in range(len(array) - 1, 0, -1):
                self.swapPlace(0, i, array)
                self.heapify(array, 0, i)
        return array

    def createMaxHeap(self, array):
        """_summary_

        Args:
            array (_type_): _description_

        Returns:
            _type_: _description_
        """
        for i in range(floor(len(array) / 2) - 1, -1, -1):
            self.heapify(array, i, len(array))
        return array

    def swapPlace(self, index1, index2, array):
        """_summary_

        Args:
            index1 (_type_): _description_
            index2 (_type_): _description_
            array (_type_): _description_
        """
        array[index1], array[index2] = array[index2], array[index1]

    def heapify(self, array, index, heapSize):
        """_summary_

        Args:
            array (_type_): _description_
            index (_type_): _description_
            heapSize (_type_): _description_
        """
        left = 2 * index + 1
        right = 2 * index + 2

        largestValueIndex = index
        if heapSize > left and array[largestValueIndex] < array[left]:
            largestValueIndex = left
        if heapSize > right and array[largestValueIndex] < array[right]:
            largestValueIndex = right

        if largestValueIndex != index:
            self.swapPlace(index, largestValueIndex, array)
            self.heapify(array, largestValueIndex, heapSize)
