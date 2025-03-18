## Self Balancing AVL Tree

AVL Trees solve an issue which Binary Search Trees are having. BST can get easily out of balance and AVL Trees tackle this issue to self balance the tree. The name AVL comes from its authors **Georgy Adelson-Velsky** and **Evgenii Landis.**

AVLs are specialized BSTs, which means that a valid AVL tree is always a BST, but not necessary the other way around. The main difference between this two is following, adding the item is literally the same in both cases, what is different is the way back, so the recursive calls to check if the node is balanced after you added the new node. A tree is out of balance when its subtree difference of heights is greater than one. The benefit of this is that we can ensure that our worst case scenario is not `O(n)` but it becomes `O(log n)` .

Let’s assume we have the following AVL tree:

```plaintext
  5

    \

      8
```

The above is a valid AVL tree and now we would like to add the node 9 to it.

```plaintext
   5 - node A

    \

      8 - node B

       \

         9 - node C
```

On the way up from the recursion we check the following:

—> check balance of node C: left height is 0, right height is 0, **balanced**

—> check balance of node B: left height is 0, right height is 1, **balanced**

—> check balance of node A: left height is 0, right height is 2, **unbalanced**, right heavy, child is right heavy

As we can see our tree is unbalanced so we need to perform a right rotation. Now we swap the values of nodes A and B. We make node B the left child of node A and make node C the right child of node A.

In the end we get the following AVL tree:

```plaintext
        8 - node A

    /       \

  5           9
 node B       node C
```
