import unittest
from frontendmasters.Complete_Intro_to_Computer_Science.recursion.recursionFactorial import (
    SolutionFactorial
)
from frontendmasters.Complete_Intro_to_Computer_Science.recursion.recursionNestedArray import (
    SolutionNestedArray
)

class TestSolution(unittest.TestCase):
    def test_recursion(self):
        solutionFactorial = SolutionFactorial()
        solutionNestedArray = SolutionNestedArray()

        self.assertEqual(solutionFactorial.recursionFactorial(5), 120)
        self.assertEqual(solutionNestedArray.recursionNestedArray([10, 5, 3, 8, 2, 6, 4, 7, 9, 1]), 55)
        self.assertEqual(solutionNestedArray.recursionNestedArray([1, [2], 3]), 6)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
