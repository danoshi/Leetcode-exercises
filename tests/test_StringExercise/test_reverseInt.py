import unittest
from StringExercise.Reverse_Integer.reverseInt import Solution


class TestSolution(unittest.TestCase):
    def test_reverse(self):
        solution = Solution()

        self.assertEqual(solution.reverse(120), 21)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
