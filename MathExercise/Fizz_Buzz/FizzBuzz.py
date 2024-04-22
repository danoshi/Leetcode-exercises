from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        erg = []

        for i in range(n):
            i += 1
            div3 = bool(i % 3 == 0)
            div5 = bool(i % 5 == 0)

            if div3 and div5:
                erg.append("FizzBuzz")
            elif div3:
                erg.append("Fizz")
            elif div5:
                erg.append("Buzz")
            else:
                erg.append(str(i))
        return erg
