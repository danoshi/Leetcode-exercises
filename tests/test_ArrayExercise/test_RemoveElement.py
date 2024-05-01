import unittest
from ArrayExercise.Remove_Element.RemoveElement import Solution


class TestSolution(unittest.TestCase):
    def test_removeElement(self):
        solution = Solution()

        self.assertEqual(solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2), 5)
        self.assertEqual(solution.removeElement2([0, 1, 2, 2, 3, 0, 4, 2], 2), 5)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
