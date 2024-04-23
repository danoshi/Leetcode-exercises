import unittest
from frontendmasters.Complete_Intro_to_Computer_Science.mergesort.mergeSort import (
    Solution
)


class TestSolution(unittest.TestCase):
    def test_mergesort(self):
        solution = Solution()

        self.assertEqual(solution.mergeSort([10, 5, 3, 8, 2, 6, 4, 7, 9, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(solution.mergeSort([10, 5, 3, 8]), [3, 5, 8, 10])
        self.assertEqual(solution.mergeSort([2, 1]), [1, 2])
        self.assertEqual(solution.mergeSort([2]), [2])

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
