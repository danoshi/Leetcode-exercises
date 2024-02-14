from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length  # Adjust k to be within the range of the array length
        while k > 0:
            # Store the last element of the array
            temp = nums[length - 1]
            print(f"temp set to nums[length -1] {temp}")
            # Shift each element to the right
            # we start at the end of the array, stop at 0, and we iterate backwards
            for i in range(length - 1, 0, -1):
                nums[i] = nums[i - 1]

            nums[0] = temp
            print(f"temp set to nums[0] {temp}")
            k -= 1

    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # much more efficient solution
        k = k % len(nums)
        print(nums[-k:])
        print(nums[:-k])
        nums[:] = nums[-k:] + nums[:-k]

test = Solution()
print(test.rotate2([1, 2, 3, 4, 5, 6, 7], 3))
#print(test.rotate([-1,-100,3,99], 2))
#test.rotate([1,2,3,4,5,6,7], 3)
