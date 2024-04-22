import unittest
from ArrayExercise.Max_Consecutive_Ones.MaxConsecutiveOnes import Solution


class TestSolution(unittest.TestCase):
    def test_findMaxConsecutiveOnes(self):
        solution = Solution()

        self.assertEqual(solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]), 3)
        self.assertEqual(solution.findMaxConsecutiveOnes([1, 1, 1, 1, 0]), 4)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
