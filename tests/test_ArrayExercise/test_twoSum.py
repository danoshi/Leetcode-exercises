import unittest
from ArrayExercise.Two_Sum.twoSum import Solution


class TestSolution(unittest.TestCase):
    def test_twoSum(self):
        solution = Solution()

        self.assertEqual(solution.twoSum([2, 7, 11, 15], 9), [1, 0])
        self.assertEqual(solution.twoSum([3, 2, 3], 6), [2, 0])

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
