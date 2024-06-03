from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def breadthFirstTraverseRecursive(self, queue, array):
        if not queue:
            return array
        node = queue.popleft()
        array.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        return self.breadthFirstTraverseRecursive(queue, array)

    def breadthFirstTraverseIterative(self, queue, array):
        queue = deque(queue)
        while len(queue):
            node = queue.popleft()
            array.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return array
