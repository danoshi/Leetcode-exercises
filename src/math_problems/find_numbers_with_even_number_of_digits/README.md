# 1295. Find Numbers with Even Number of Digits

Let’s have a look on the description of the problem:

Given an array `nums` of integers, return how many of them contain an **even number** of digits.

**Example 1:**

```
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.
```

In this problem we had to use our math skills since this required some knowledge on how to get one by one every digit of a number. Let’s have a look on my solution:

1. First I initialize two variables, one called digits which I set to `0` and the next one counter which I also set to `0`.
2. Now I `for loop` through the array which is passed into the function. Now in the for loop I create a `while loop` with the condition to run so long until x which is my current element from the array, is bigger than 0.
3. Next I divide my current element `x` with `10` and use the `math.floor` function the round it down. Additionally, after the calculation we add one to our digits variable since it our element x has at least one digit.
4. As a next step we take the digits variable and set up an if condition which checks `if digits modulo two equals 0` . If this is the case we would add `1` to the counter. After we are done with the first element of `x` we set the digits variable to `0` to again count it for the next element.
5. In the end we `return` the `counter` which tells us how many numbers in the array have an even digit count.

Time Complexity: `Big O(n²)`, where `n` is the number of elements in the array.
Space Complexity: `Big O(1)` . I did not use any additional space.
