# 905. Sort Array By Parity

Given an integer array `nums`, move all the even integers at the beginning of the array followed by all the odd integers.

Return **\*any array** that satisfies this condition\*.

**Example 1:**

```
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

```

**Example 2:**

```
Input: nums = [0]
Output: [0]
```

In this problem we need to take all the even numbers and bring them in front of the array and the even to the back so that when someone is looking at the array there is a clear separation of elements visible. The easiest way to check if a number is even or odd is to check the remainder of it when doing modulo by two. Let’s have a look at my solution:

1. First I initialize two variables which will be my pointers. I use in this problem a `two pointer` solution. I call them `r` and `l` which stands for right and left.
2. Now I do a `while loop` which is running so long until my right variable is smaller than the length of the array.
3. In the body of the while loop I have a `if condition` which is checking the `r` element which is my current element of the array if the remainder of the `modulo` operation is `0`.
4. If this is the case I switch the `l` element which is ensuring that the left side of the array has the even numbers with the `r` element which is going one by one through the array checking the elements which one is even and which one is odd.
5. Now that the switch happened I increment the `l` variable by one since the switch happened, and I am sure of that my first element is an even number.
6. After the `if condition` I increment the `r` variable by one.
7. Last but not least we return the modified array.

**Big O**

- Time Complexity: `Big O(n)`, where `n` is the number of elements in the array.
- Space Complexity: `Big O(1)` . I did not use any additional space.
