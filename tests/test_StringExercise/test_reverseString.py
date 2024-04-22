import unittest
from StringExercise.Reverse_String.reverseString import (
    Solution
)


class TestSolution(unittest.TestCase):
    def test_reverseString(self):
        solution = Solution()

        self.assertEqual(solution.reverseString(["h", "e", "l", "l", "o"]), None)
        self.assertEqual(solution.reverseString2(["h", "e", "l", "l", "o"]), None)
        self.assertEqual(solution.reverseString3(["h", "e", "l", "l", "o"]), None)

    def tearDown(self):
        print("All tests passed successfully!")

if __name__ == "__main__":
    unittest.main()
