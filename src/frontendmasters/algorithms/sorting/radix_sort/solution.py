class Solution:
    def getDigit(self, number, place, longestNum):
        """_summary_

        Args:
            number (_type_): _description_
            place (_type_): _description_
            longestNum (_type_): _description_

        Returns:
            _type_: _description_
        """
        chars = str(number)
        size = len(chars)
        mod = longestNum - size
        index = place - mod
        if 0 <= index < size:
            return chars[index]
        else:
            return 0

    def getLongestNumber(self, arr):
        """_summary_

        Args:
            arr (_type_): _description_

        Returns:
            _type_: _description_
        """
        longest = 0
        for i in range(0, len(arr)):
            currentlen = len(str(arr[i]))
            if currentlen > longest:
                longest = currentlen
        return longest

    def radixSort(self, array):
        """_summary_

        Args:
            array (_type_): _description_

        Returns:
            _type_: _description_
        """
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
