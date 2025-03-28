import unittest
import sys
from collections import deque
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
from src.frontendmasters.algorithms.tree_traversal.breadth_first.solution import TreeNode, Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        # Create a binary tree to use in the tests
        #       1
        #      / \
        #     2   3
        #    / \
        #   4   5
        self.root = TreeNode(1)
        self.root.left = TreeNode(2)
        self.root.right = TreeNode(3)
        self.root.left.left = TreeNode(4)
        self.root.left.right = TreeNode(5)
        self.solution = Solution()

    def test_breadthFirstTreeTraversals_recursion(self):
        expected = [1, 2, 3, 4, 5]
        result = self.solution.breadthFirstTraverseRecursive(deque([self.root]), [])
        self.assertEqual(result, expected)

    def test_breadthFirstTreeTraversals_iterative(self):
        expected = [1, 2, 3, 4, 5]
        result = self.solution.breadthFirstTraverseIterative(deque([self.root]), [])
        self.assertEqual(result, expected)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
