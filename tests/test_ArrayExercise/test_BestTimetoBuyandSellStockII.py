import unittest
from ArrayExercise.Best_Time_to_Buy_and_Sell_Stock_II.BestTimetoBuyandSellStockII import (
    Solution
)

class TestSolution(unittest.TestCase):
    def test_maxProfitA(self):
        solution = Solution()

        self.assertEqual(solution.maxProfitA([1,2,3,4,5]), 4)
        self.assertEqual(solution.maxProfitA([7,1,5,3,6,4]), 7)
        self.assertEqual(solution.maxProfitA([7,6,4,3,1]), 0)
        self.assertEqual(solution.maxProfitA([7,1,5,3,6,4]), 7)

    def tearDown(self):
        print("All tests passed successfully!")

if __name__ == "__main__":
    unittest.main()
