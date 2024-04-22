import unittest
from ArrayExercise.Remove_Duplicates_from_Sorted_Array.removeDuplicateItem import (
    Solution,
)
from ArrayExercise.Remove_Duplicates_from_Sorted_Array.duplicateItemLeetcodeSolution import (
    Solution2,
)


class TestSolution(unittest.TestCase):
    def test_removeDuplicates(self):
        solution_leetcode = Solution2()
        solution = Solution()

        self.assertEqual(solution_leetcode.removeDuplicates([1, 1, 2]), 2)
        self.assertEqual(solution.removeDuplicates([1, 1, 2]), 2)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
