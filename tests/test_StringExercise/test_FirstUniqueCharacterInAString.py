import unittest
from StringExercise.First_Unique_Character_in_a_String.FirstUniqueCharacterInAString import (
    Solution,
)


class TestSolution(unittest.TestCase):
    def test_firstUniqChar(self):
        solution = Solution()

        self.assertEqual(solution.firstUniqChar("leetcode"), 0)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
