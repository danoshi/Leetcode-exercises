import unittest
from frontendmasters.Complete_Intro_to_Computer_Science.DepthFirstTreeTraversals.depthFirstTreeTraversals import (
    Solution,
    TreeNode,
)


class TestSolution(unittest.TestCase):
    def setUp(self):
        # Create a binary tree to use in the tests
        #       1
        #      / \
        #     2   3
        #    / \
        #   4   5
        self.tree = TreeNode(1)
        self.tree.left = TreeNode(2)
        self.tree.right = TreeNode(3)
        self.tree.left.left = TreeNode(4)
        self.tree.left.right = TreeNode(5)
        self.solution = Solution()

    def test_preorder_traversal(self):
        expected = [1, 2, 4, 5, 3]
        result = self.solution.preorderTraversals(self.tree, [])
        self.assertEqual(result, expected)

    def test_inorder_traversal(self):
        expected = [4, 2, 5, 1, 3]
        result = self.solution.inorderTraversals(self.tree, [])
        self.assertEqual(result, expected)

    def test_postorder_traversal(self):
        expected = [4, 5, 2, 3, 1]
        result = self.solution.postorderTraversals(self.tree, [])
        self.assertEqual(result, expected)

    def tearDown(self):
        print("All tests passed successfully!")


if __name__ == "__main__":
    unittest.main()
