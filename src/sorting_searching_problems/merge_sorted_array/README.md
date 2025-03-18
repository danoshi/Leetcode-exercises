# 88. Merge Sorted Array

Let's have a look on the description of the problem:

You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.

**Merge** `nums1` and `nums2` into a single array sorted in **non-decreasing order**.

The final sorted array should not be returned by the function, but instead be _stored inside the array_ `nums1`. To accommodate this, `nums1` has a length of `m + n`, where the first `m` elements denote the elements that should be merged, and the last `n` elements are set to `0` and should be ignored. `nums2` has a length of `n`.

**Example 1:**

```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
```

For this problem I was mainly thinking outside the box and came to a very elegant solution. Let’s have a deeper look into my solution:

1. I created a new array where I merge the two arrays together and initialize it as empty for now.
2. Now I shallow copy both of the arrays into my new one and use the python slicing mechanism starting from the first element until the element which is specified. After this I have all the elements which I want in my new array.
3. Next I need to sort the array to have it in order, so I just the built-in python function `sort()`.
4. In the last step I shallow copy the initial array to the one I created and now the array has the correct reference.

The time and space complexity for this would be `Big O(n)`.
