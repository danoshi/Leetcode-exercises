class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """_summary_

        Args:
            n (int): _description_

        Returns:
            bool: _description_
        """
        count = 0
        erg = 0
        while erg <= n:
            erg = pow(3, count)
            if erg == n:
                return True
            count += 1
        return False
