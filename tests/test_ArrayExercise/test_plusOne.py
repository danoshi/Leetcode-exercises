import unittest
from ArrayExercise.Plus_One.plusOne import (
    Solution
)

class TestSolution(unittest.TestCase):
    def test_plusOne(self):
        solution = Solution()

        self.assertEqual(solution.plusOne([1,2,3]), [1,2,4])
        self.assertEqual(solution.plusOne([9]), [1,0])
        self.assertEqual(solution.plusOne([9,9,9]), [1,0,0,0])

    def tearDown(self):
        print("All tests passed successfully!")

if __name__ == "__main__":
    unittest.main()
