# 1089. Duplicate Zeros

Let’s have a look on the description of the problem:

Given a fixed-length integer array `arr`, duplicate each occurrence of zero, shifting the remaining elements to the right.

**Note** that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

**Example 1:**

```
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
```

In this problem we would need to duplicate the zero elements and shift the elements to the right side, which would mean whenever we duplicate we would pop the last element. Let’s have a more detailed look on my solution:

1. I created a variable called zeros where I count all the `0` from the array. Moreover, a second variable was created which stores the length of the array.
2. Now I use an `for loop` to loop backward over the list starting from the last index and ending on index `0` . I also decrement by 1 each time.
3. Now I check if my current element plus the variable zeros are smaller than the length of the array. This ensures that we are still in range. If this is the case I shift the element at index `i` to the right by `zeros` positions. This ensures that the `0` is successfully duplicated.
4. In the next step I check if my current element is `0` and if this is the case I subtract `1` from the `zeros` .
5. Last but not least after updating the zeros value I check again the same if condition is my current element plus the variable zeros are smaller than the length of the array. If this is the case I shift the element at index `i` to the right by `zeros` positions. This ensures that the `0` is successfully duplicated.

**Big O**

- Time Complexity: `Big O(n)`, where `n` is the number of elements in the array.
- Space Complexity: `Big O(1)` . I did not use any additional space.
