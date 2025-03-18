class Solution:
    def recursion_factorial(self, n):
        """_summary_

        Args:
            n (_type_): _description_

        Returns:
            _type_: _description_
        """
        if n == 1:
            return 1
        elif n <= 0:
            return 0
        # the recursive call calculating it so often until n hits 1
        return n * self.recursion_factorial(n - 1)

    def recursion_nested_array(self, nums):
        """_summary_

        Args:
            nums (_type_): _description_

        Returns:
            _type_: _description_
        """
        erg = 0
        for i in range(len(nums)):
            current = nums[i]
            # if current is a nested array call the function again with the array
            if isinstance(current, list):
                erg += self.recursion_nested_array(current)
            # if it's a number just add it to the sum
            else:
                erg += current
        return erg
