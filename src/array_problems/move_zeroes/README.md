# 283. Move Zeroes

Let's have a look on the description of the problem:

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

**Note** that you must do this in-place without making a copy of the array.

**Example 1:**

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

```

My approach to the problem was following, since all the 0 need to be moved to the end, and we are not able to sort the array because we need to maintain the relative order what I did was delete all the 0 in the array, count how many times there was a 0 and then append it to the end `n` times.

1. First of all I create a variable for the length of the array, a counter and a bool variable to keep track if there are multiple 0 in the beginning of the array.
2. Now if the array is of length 1 or 0, just return it if not go to the while loop and in the while loop we set our condition to false since if there is any 0 in the array we can just stop, but if there is one we remove it, add to the counter 1 and set the bool variable to true again since it should start over. This happens `n` until all the 0 are deleted in the array.
3. In the last step we create again a while loop and set the condition bigger than 0 so that we append `n` times our 0 to the array.

In the end we have our array which has its relative order and all the zero elements in the end. The time complexity is Big O of `O(n²)` .
