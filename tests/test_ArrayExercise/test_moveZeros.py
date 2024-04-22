import unittest
from ArrayExercise.Move_Zeroes.moveZeros import Solution


class TestSolution(unittest.TestCase):
    def test_moveZeroes(self):
        solution = Solution()

        self.assertEqual(solution.moveZeroes([4, 2, 4, 0, 0, 3, 0, 5, 1, 0]), None)
        self.assertEqual(solution.moveZeroes2([0, 0, 1]), None)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
