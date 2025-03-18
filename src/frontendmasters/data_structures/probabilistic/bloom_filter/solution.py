class Solution:
    def __init__(self):
        """_summary_"""
        self._array = [0] * 100

    def _h1(self, string):
        return abs(hash("abcd" + string)) % 100

    def _h2(self, string):
        return abs(hash("1234" + string)) % 100

    def _h3(self, string):
        return abs(hash("6789" + string)) % 100

    def add(self, string):
        self._array[self._h1(string)] = 1
        self._array[self._h2(string)] = 1
        self._array[self._h3(string)] = 1

    def contains(self, string):
        """_summary_

        Args:
            string (_type_): _description_

        Returns:
            _type_: _description_
        """
        return all(
            [
                self._array[self._h1(string)],
                self._array[self._h2(string)],
                self._array[self._h3(string)],
            ]
        )
