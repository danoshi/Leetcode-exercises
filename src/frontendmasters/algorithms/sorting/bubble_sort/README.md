## Bubble Sort

The algorithm is pretty simple: compare two items in an array that are next to each other. If they're out of order (that is, the larger one comes first in the array) swap them. Then move forward one index, compare again, swap if needed, and continue to the next item in the array. Once we've reached the end of the array, if we've swapped
anything in the previous run through, the array _could_ still be out of order, so we have to pass through again. Once we run through the whole array with no swaps, the array is sorted!

| 1   | 5   | 4   | 2   | 3   |
| --- | --- | --- | --- | --- |

Bubble Sort will start comparing 1 with 5, if 1 is bigger than 5. This is not the same, so we leave 1 at the index it is currently. Now we go with 5 and compare it with 4, this time 5 is bigger than 4, so we switch 4 and 5. In the next step we look at 5 which swapped places with 4 and look if 5 is bigger than 2, this is the case, so we again swap 5, and we do this until the end of the array. Because when 5 is on the last index of our array we still need to sort the other elements so bubble sort will again go from beginning to end so that the array is fully sorted.

1. 1 > 5 = False
2. 5 > 4 = True
3. 5 > 2 = True
4. 5 > 3 = True

After the first bubble sort our array would look like this:

| 1   | 4   | 2   | 3   | 5   |
| --- | --- | --- | --- | --- |

1. 1 > 4 = False
2. 4 > 2 = True
3. 4 > 3 = True
4. 4 > 5 = False

And after the second iteration we have our sorted array.

| 1   | 2   | 3   | 4   | 5   |
| --- | --- | --- | --- | --- |
