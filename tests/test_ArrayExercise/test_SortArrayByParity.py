import unittest
from ArrayExercise.Sort_Array_By_Parity.SortArrayByParity import (
    Solution
)


class TestSolution(unittest.TestCase):
    def test_sortArrayByParity(self):
        solution = Solution()

        self.assertEqual(solution.sortArrayByParity([3,1,2,4]), [2, 4, 3, 1])
        self.assertEqual(solution.sortArrayByParity([0]), [0])

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
