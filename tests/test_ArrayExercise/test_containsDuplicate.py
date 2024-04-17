import unittest
from ArrayExercise.Contains_Duplicate.containsDuplicate import (
    Solution
)

class TestSolution(unittest.TestCase):
    def test_containsDuplicate(self):
        solution = Solution()

        self.assertEqual(solution.containsDuplicate2([0,4,5,0,3,6]), True)
        self.assertEqual(solution.containsDuplicate([0,4,5,0,3,6]), True)
        self.assertEqual(solution.containsDuplicate2([1,2,3,4,5]), False)
        self.assertEqual(solution.containsDuplicate([1,2,3,4,5]), False)

        self.assertEqual(solution.containsDuplicate2([3,3]), True)
        self.assertEqual(solution.containsDuplicate([3,3]), True)

    def tearDown(self):
        print("All tests passed successfully!")

if __name__ == "__main__":
    unittest.main()
