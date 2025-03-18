# 977. Squares of a Sorted Array

Let’s have a look on the description of the problem:

Given an integer array `nums` sorted in **non-decreasing** order, return _an array of **the squares of each number** sorted in non-decreasing order_.

**Example 1:**

```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
```

There are multiple ways on how to tackle the following problem. It could be done without using additional space, or with to store the new values in an array. Let’s have a look how I solved it:

1. I created an additional array where I want to store the squares of each number.
2. Now I use a `for loop` to loop through the elements in the array which is passed as an argument by the function.
3. As a next step we multiply the element with itself and the result is being appended to the array which was created in the beginning.
4. Last but not least we use the python built in `sort()` function to have the array sorted in non-decreasing order. In the end we return our array which we created in the beginning.

This could be easily done without the additional space just replacing the current value with the result of the multiplication but for me this solution was cleaner.

Time Complexity: `Big O(n)`, where `n` is the number of elements in the array.
Space Complexity: `Big O(n)` . I use an additional array.
