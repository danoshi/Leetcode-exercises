import unittest
from ArrayExercise.Replace_Elements_with_Greatest_Element_on_Right_Side.ReplaceElementswithGreatestElementonRightSide import (
    Solution
)


class TestSolution(unittest.TestCase):
    def test_replaceElements(self):
        solution = Solution()

        self.assertEqual(solution.replaceElements([17,18,5,4,6,1]), [18, 6, 6, 6, 1, -1])
        self.assertEqual(solution.replaceElements([400]), [-1])

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
