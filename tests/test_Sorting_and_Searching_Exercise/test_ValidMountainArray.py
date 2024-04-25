import unittest
from Sorting_and_Searching_Exercise.Valid_Mountain_Array.ValidMountainArray import (
    Solution,
)


class TestSolution(unittest.TestCase):
    def test_validMountainArray(self):
        solution = Solution()

        self.assertEqual(solution.validMountainArray([2, 1]), False)
        self.assertEqual(solution.validMountainArray([3, 5, 5]), False)
        self.assertEqual(solution.validMountainArray([0, 3, 2, 1]), True)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
