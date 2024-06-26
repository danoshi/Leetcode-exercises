from typing import List


class SolutionFactorial:
    def recursionFactorial(self, n):
        if n == 1:
            return 1
        elif n <= 0:
            return 0
        # the recursive call calculating it so often until n hits 1
        return n * self.recursionFactorial(n - 1)
