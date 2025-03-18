## ArrayList

If we would not have arrays and only object, how we would need to implement a class to create arrays, call the methods like adding numbers, getting a number, deleting etc.

For array list, this works more or less how we as humans tend think about it: in memory we'll lay out everything sequentially in memory. Just by knowing where the start of the array is and the index, we know where the thing we're looking for in memory. This would be a O(1) in terms of complexity. No matter how big the ArrayList is, array lookups take the same amount of time.

Now imagine our list is 15,000 items long, and we delete the 1 index. We now have to shift 14,998 items over in memory. This is called compacting, and it's painful for ArrayList. Same applies for inserts.
