class Solution:
    def romanToInt(self, s: str) -> int:
        """_summary_

        Args:
            s (str): _description_

        Returns:
            int: _description_
        """
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        i = 0
        while i < len(s):
            # If this is the subtractive case.
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                total += roman[s[i + 1]] - roman[s[i]]
                i += 2
            # Else this is NOT the subtractive case.
            else:
                total += roman[s[i]]
                i += 1
        return total
