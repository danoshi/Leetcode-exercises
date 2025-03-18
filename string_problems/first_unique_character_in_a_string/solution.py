from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        """_summary_

        Args:
            s (str): _description_

        Returns:
            int: _description_
        """
        counter = Counter(s)

        for i, c in enumerate(s):
            if counter[c] == 1:
                return i

        return -1
