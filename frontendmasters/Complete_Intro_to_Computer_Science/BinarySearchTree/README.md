## Binary Search Tree

Trees are another way to structure data. Binary search trees work differently than arrays and have their own use case. Binary Search Tree have to be sorted and if we add an element to it, it will be in a sorted fashion. They are always modelled in a way that we have a root node on top and everything on the left side of the tree is smaller than the root node and everything on the right side is lager then the root node. The lookups in a binary search is in average case Big `O(log n)` . Databases are using mostly tree structures for lookup of indexes.

For example with the following Tree structure:

10 as a root node → 11 as a right child node since it's larger than the root node → and then 6 as a child node on the left side since its smaller than 10.

When we want to add now 5 we would do the following:

1. Check where to put 5, it's smaller than 10, so it will be on the left side.
2. Now 6 is a child of 10, and it's bigger than 5 so 5 will be a new child of 6.
3. It will be in the middle since it doesn’t have any neighbours.
4. Will there any new node came which is smaller than 5 we will move then the child node from 6 so the 5 on the right side and the smaller one on the left side.
