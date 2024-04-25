# 941. Valid Mountain Array

Given an array of integers `arr`, return _`true` if and only if it is a valid mountain array_.

Recall that arr is a mountain array if and only if:

- `arr.length >= 3`
- There exists some `i` with `0 < i < arr.length - 1` such that:
  - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`
  - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

**Example 1:**

```
Input: arr = [2,1]
Output: false
```

In this problem we would need to check each an every element to see when we hit the peak which can’t be the start and as well it can’t be the end. We also need to check that when we find the peak that each next element is smaller than the next one, so we can make sure that we walk down from the peak. Let’s have a more detailed look on my solution:

1. First we need to check if the length of the array is smaller than 3. If this is the case we can immediately `return False` .
2. Now we initialize a variable called `i` which we set to 0 and in the next line we create a `while loop` where we first check if our `i` is in the range of the array and that our current element `arr[i]` is smaller than the next item in the array which would be `arr[i+1]` . With this check we make sure that we walk the mountain up. If all the condition are met we add one to our `i` .
3. Next we need to make sure that our top of the mountain is not the first or last element since then it would not be a valid mountain. We check if our variable `i` is zero or our `i` is the length of the array. Since we had our first while loop we can make sure that we are at the peak which should be somewhere in the middle of the array, so checking if `i` is zero or the length of the array would make sure that we have a valid mountain. If after the first while loop our `i` is `0` or `len(arr) - 1` then we `return False` .
4. As a next step we make a new while loop which again will run until `i` is in the range of the array and now my current element which is `arr[i]` needs to be greater than the next element which is `arr[i + 1]` with that we make sure that we walk down the mountain. If these conditions are met we add one to our `i` .
5. Last but not least we return `True` if our `i` is equal to the `len(arr) - 1` else `False`.

**Big O**

- Time Complexity: `Big O(n)`, where `n` is the number of elements in the array.
- Space Complexity: `Big O(1)` . I did not use any additional space.
