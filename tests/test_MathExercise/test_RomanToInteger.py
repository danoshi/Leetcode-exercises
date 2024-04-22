import unittest
from MathExercise.Roman_to_Integer.RomanToInteger import Solution


class TestSolution(unittest.TestCase):
    def test_romanToInt(self):
        solution = Solution()

        self.assertEqual(solution.romanToInt("MCMXCIV"), 1994)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
