from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()


test = Solution()
print(test.singleNumber([2, 2, 1]))  # 1
# print(test.singleNumber([4,1,2,1,2])) # 4
# print(test.singleNumber([1])) # 1
