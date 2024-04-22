import unittest
from Sorting_and_Searching_Exercise.Merge_Sorted_Array.MergeSortedArr import (
    Solution
)


class TestSolution(unittest.TestCase):
    def test_merge(self):
        solution = Solution()

        self.assertEqual(solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), None)
        self.assertEqual(solution.merge([1], 1, [], 0), None)
        self.assertEqual(solution.merge([0], 0, [1], 1), None)


    def tearDown(self):
            print("All tests passed successfully!")

if __name__ == "__main__":
    unittest.main()
