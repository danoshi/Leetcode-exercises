# 27. Remove Element

Let’s have a look on the description of the problem:

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)**. The order of the elements may be changed. Then return _the number of elements in_ `nums` _which are not equal to_ `val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

**Example 1:**

```
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

In this problem we need to remove all the occurrences of an element in an array and return the new length of the array, but we have the constraint to not use an additional array since we need to do it in place. Let’s have a look into my solution:

1. I first create a variable named `counter` to store the count of a specific value provided as an argument to the function. This variable indicates the frequency of occurrence of the specified value within the array.
2. Next I created a `while loop` which runs so long until our counter is greater than `0` . In this while loop we have another `for loop` to go through the elements in the array.
3. Now we check if the current element of the array is equal to the value which is passed to the function. If yes we use the built-in python function `remove` to delete the element. Additionally, we subtract minus `1` to the counter.
4. In the end, we return the updated length of the array by utilizing the `len` method directly on the array.

Time Complexity: `Big O(n²)`, where `n` is the number of elements in the array.
Space Complexity: `Big O(1)` . I did not use any additional space.
