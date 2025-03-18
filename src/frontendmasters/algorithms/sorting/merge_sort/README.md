### Merge Sort

Merge Sort by definition takes the array which needs to be sorted break it down into smaller arrays so long until the length of the array is 1 or 0. It is doing this because an array of length 1 or 0 is sorted by definition since there is only one or zero elements in there. In the next step Merge Sort is taking this arrays of length 1 or 0 and is combining it together but here it checks is the first element (the only element) bigger then the other element from the other array. If its smaller it appends it to the front, if its bigger it will append it to the end.

In merge sort we need `two functions` . The first breaks down the array into smaller arrays (which is our recursive function) and the other is a function that takes two `sorted` arrays and returns back one sorted array.

In the example above you can see an unsorted array split into arrays of length 1 or 0. Afterward our merge function combine this arrays and checking weather the one and only element is bigger than the other one. In the end we get the sorted array.

In merge sort the `best case / worst case / average case` have the same `Big O`, since no matter how sorted the array is, it will split it up into arrays of length one or zero and then combine it back together. Since every item in the array has to be looked at least once we are going to have `Big O(n)` .

Since not every item needs to be checked with every other item in the arrays, for example we have `[1, 2]` and `[4, 7]` , 7 will be not compared with 1 or 2 because since 4 is bigger than 1 and 2 and the list is already sorted it will be appended to the end of the arrays after 4. So with more items in the array our `Big O` will change eventually to be `log n`.

So we combine now the both scenarios and have the Big O for merge sort which is `O(n log n)` .

For the space complexity since we create for every item an array our Big O is `O(n)`
