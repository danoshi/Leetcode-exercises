import unittest
from ArrayExercise.Rotate_Array.rotatearray import (
    Solution
)

class TestSolution(unittest.TestCase):
    def test_rotate(self):
        solution = Solution()

        self.assertEqual(solution.rotate([1, 2, 3, 4, 5, 6, 7], 3), None)
        self.assertEqual(solution.rotate2([1, 2, 3, 4, 5, 6, 7], 3), None)

        self.assertEqual(solution.rotate([-1,-100,3,99], 2), None)
        self.assertEqual(solution.rotate2([-1,-100,3,99], 2), None)

    def tearDown(self):
        print("All tests passed successfully!")

if __name__ == "__main__":
    unittest.main()
