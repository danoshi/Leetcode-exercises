import unittest
from Sorting_and_Searching_Exercise.Duplicate_Zeros.DuplicateZeros import (
    Solution
)


class TestSolution(unittest.TestCase):
    def test_duplicateZeros(self):
        solution = Solution()

        self.assertEqual(solution.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]), None)

    def tearDown(self):
        print("All tests passed successfully!")

if __name__ == "__main__":
    unittest.main()
