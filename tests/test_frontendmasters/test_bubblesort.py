import unittest
from frontendmasters.Complete_Intro_to_Computer_Science.bubblesort.bubblesort import (
    Solution,
)


class TestSolution(unittest.TestCase):
    def test_bubblesort(self):
        solution = Solution()

        self.assertEqual(
            solution.bubbleSort([10, 5, 3, 8, 2, 6, 4, 7, 9, 1]),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        )
        self.assertEqual(solution.bubbleSort([10, 5, 3, 8]), [3, 5, 8, 10])
        self.assertEqual(solution.bubbleSort([2, 1]), [1, 2])
        self.assertEqual(solution.bubbleSort([2]), [2])

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
