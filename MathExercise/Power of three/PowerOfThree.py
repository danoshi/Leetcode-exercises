class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        count = 0
        erg = 0
        while erg <= n:
            erg = pow(3, count)
            if erg == n:
                return True
            count += 1
        return False


test = Solution()
print(test.isPowerOfThree(3))
