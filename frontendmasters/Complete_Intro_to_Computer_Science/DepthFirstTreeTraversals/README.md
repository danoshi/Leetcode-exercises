## Depth First Tree Traversals

Traversals are needed when you serialize the entire tree into a flat data structure. For example, we have a valid BST, and we would like to get all the node values into an array. There would be three variations of depth-first traversal how you could achieve it.

- pre-order traversal
    - This process the node starting from the root node going to the left subtree and then to the right subtree.
- inorder traversal
    - This process the node starting from the left subtree going to the root node and then to the right subtree.
- postorder traversal
    - This process the node starting from the left subtree but with going forward with all the nodes first which do not have a child. After that it will go to the right subtree first to the nodes without child and in the end the root node.

All of them have their own use case. Preorder traversal is useful when you want to make a deep copy of a tree, since you do copy a node and then add its left child and then its right tree. If you have a BST you do want to use inorder. Postorder traversal use case is when you want to delete the tree since it would go from the left childs to the right ones and in the end go to the root node.
