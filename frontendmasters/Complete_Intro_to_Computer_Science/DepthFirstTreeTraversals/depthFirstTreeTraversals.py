
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:

    def preorderTraversals(self, node, array):
        if not node:
            return array
        array.append(node.value)
        array = self.preorderTraversals(node.left, array)
        array = self.preorderTraversals(node.right, array)
        return array


    def inorderTraversals(self, node, array):
        if not node:
            return array
        array = self.inorderTraversals(node.left, array)
        array.append(node.value)
        array = self.inorderTraversals(node.right, array)
        return array


    def postorderTraversals(self, node, array):
        if not node:
            return array
        array = self.postorderTraversals(node.left, array)
        array = self.postorderTraversals(node.right, array)
        array.append(node.value)
        return array
