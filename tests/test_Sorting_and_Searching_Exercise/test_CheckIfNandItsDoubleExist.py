import unittest
from Sorting_and_Searching_Exercise.Check_If_N_and_Its_Double_Exist.CheckIfNandItsDoubleExist import (
    Solution,
)


class TestSolution(unittest.TestCase):
    def test_checkIfExist(self):
        solution = Solution()

        self.assertEqual(solution.checkIfExist([-2, 0, 10, -19, 4, 6, -8]), False)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
