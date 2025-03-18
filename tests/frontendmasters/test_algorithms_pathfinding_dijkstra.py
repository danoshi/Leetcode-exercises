import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from src.frontendmasters.algorithms.pathfinding.dijkstra.solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_pathfinding(self):
        start_a = (0, 0)
        start_b = (4, 3)
        maze = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0]]
        path = self.solution.find_shortest_path_length(maze, start_a, start_b)
        expected = 7
        self.assertEqual(path, expected)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
