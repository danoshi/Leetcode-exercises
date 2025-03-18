import unittest
import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).parent.parent.parent))

from src.array_problems.best_time_to_buy_and_sell_stock_ll.solution import Solution

class TestSolution(unittest.TestCase):
    def test_max_profit_a(self):
        solution = Solution()

        self.assertEqual(solution.maxProfitA([1, 2, 3, 4, 5]), 4)
        self.assertEqual(solution.maxProfitA([7, 1, 5, 3, 6, 4]), 7)
        self.assertEqual(solution.maxProfitA([7, 6, 4, 3, 1]), 0)
        self.assertEqual(solution.maxProfitA([7, 1, 5, 3, 6, 4]), 7)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
