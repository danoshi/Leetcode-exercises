import unittest
from MathExercise.Fizz_Buzz.FizzBuzz import Solution


class TestSolution(unittest.TestCase):
    def test_fizzBuzz(self):
        solution = Solution()

        self.assertEqual(
            solution.fizzBuzz(15),
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "FizzBuzz",
            ],
        )

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
