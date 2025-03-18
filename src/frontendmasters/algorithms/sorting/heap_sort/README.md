## Heap Sort

> A heap is an array that represents a tree data structure and has to be sorted in a particular way to represent that tree. Priority queues are often represented as heaps and often those two terms are used interchangeably even if the priority queue is implemented a different way.

To explain a priority queue, we can think of internet traffic and how it handles data packets. For example, if we are watching Netflix in one browser tab and in another tab, we have Google Drive where we are uploading something or syncing to our local machine, it would prioritize the Netflix tab. The reason for this is that when we watch something, we do not want the stream to lag or to be in a loading state. On the other hand, the upload or sync can lose some packets since we do not need it synced or uploaded immediately. This is an example of a priority queue, and these are usually stored as heaps.

In our example we will talk about binary heaps but keep in mind there are other as well. A binary heap is an array, in comparison to a BST which is made up of node objects. In a BST there is a strict order where a left child is which is not true for binary heap. Binary heap guarantee that the parent is always greater than the children but there is no guarantees between sibling nodes.

The process of heapsort is following:

1. Make the array a max heap and for that, you’ll run the heapify on the first half of the array, going backwards.
2. Loop over the array / max array, dequeuing the root node, which will give the largest item. Now we swap the root node with the last item in the array to ensure that our last item is now the biggest in the array.
3. After dequeing each item, the heapify function will be run to find the next root node
4. In the next loop we will dequeue the new root node and swap it with the second to last item in the array and run heapify again.
5. We are finished when there are no items to dequeue and the array is sorted.

**Big O**

- Time Complexity: `Big O(n log (n))`, where `n` is the number of elements in the array.
