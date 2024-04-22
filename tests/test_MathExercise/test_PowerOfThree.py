import unittest
from MathExercise.Power_of_three.PowerOfThree import (
    Solution
)


class TestSolution(unittest.TestCase):
    def test_isPowerOfThree(self):
        solution = Solution()

        self.assertEqual(solution.isPowerOfThree(3), True)

    def tearDown(self):
        print("All tests passed successfully!")

if __name__ == "__main__":
    unittest.main()
