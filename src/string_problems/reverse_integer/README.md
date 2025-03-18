# 7. Reverse Integer

Let’s have a look on the description of the problem:

Given a signed 32-bit integer `x`, return `x` _with its digits reversed_. If reversing `x` causes the value to go outside the signed 32-bit integer range `[-231, 231 - 1]`, then return `0`.

**Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

**Example 1:**

```
Input: x = 123
Output: 321
```

This problem was really challenging since I do not know how to tackle it. At, first it was important that the value do not go outside the signed 32-bit integer range. Next we need to `loop` through the `int number` to get one number at the time. Let’s have a more detailed look on the solution:

1. First we need to define three variables one which is the maximal 32-bit integer number, one which is the minimal 32-bit number and one which will store our reverse value.
2. Next we create a `while loop` where we check if my number which I need to reverse is not 0, so it will stop when all elements of the numbers are reverse.
3. In the loop I create an if condition which checks the `reversed number` if it is still in the range of the min and max 32-bit integer range.
4. If this is not the case we calculate the modulo ten of the number and add the number to the reverse variable. We also multiply the reverse variable with ten so that the new digit is appended to the last place because if we would not do it, it would add up to the current number which would modify the number.
5. In the last step we could divide by ten or use `math.trunc` to get rid of the last element in our number. We do this so long until we reversed the whole number.

The time complexity would be `Big O (log(n))` since we always get rid of the last element of our int and as well if we exceed the range of max min integer we would stop. The space Complexity is `Big O(1)` since we do not use any additional space.
