from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits) - 1
        if digits[length] < 9:
            digits[length] += 1
            return digits
        else:
            for n in reversed(
                range(length + 1)
            ):  # Include length+1 to iterate over all digits
                if digits[n] < 9:
                    digits[n] += 1
                    return digits
                else:
                    digits[n] = (
                        0  # Set the digit to 0 and continue to the next iteration
                    )
            # If we reach this point, it means all digits were 9, so we need to add an extra digit
        digits.insert(0, 1)
        return digits
