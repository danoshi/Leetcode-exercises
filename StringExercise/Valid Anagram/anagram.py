class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = []
        arr2 = []
        for x in s:
            arr.append(x)
        for i in t:
            arr2.append(i)
        arr.sort()
        arr2.sort()

        if arr2 == arr:
            return True
        return False


test = Solution()
print(test.isAnagram("anagram", "nagaram"))
