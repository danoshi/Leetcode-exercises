# 326. Power of Three

Let’s have a look on the description of the problem:

Given an integer `n`, return *`true` if it is a power of three. Otherwise, return `false`*.

An integer `n` is a power of three, if there exists an integer `x` such that `n == 3x`.

**Example 1:**

```
Input: n = 27
Output: true
Explanation: 27 = 33
```

I approached the problem with the thought that if `n` is a power of three integer, then by counting up all the powers of three, I would eventually reach the desired number. Let’s have a more detailed look on my solution:

1. I start by initializing two helper variables, both set to zero. One variable will store the result from the power of three calculation, while the other will count up to determine the next power of three.
2. Next, I create a `while loop` with the condition to run until my helper variable result is less than or equal to the parameter given to the function.
3. Within the loop, we use the `pow` function from the math module to traverse the power of three sequence. We stop when our sequence value exceeds the value passed to the function.
4. If our power of three result matches the passed value, we terminate the loop and `return True`. Otherwise, we increment our helper variable 'count' by one, and eventually, the loop stops, `returning False` since the passed value is not in the power of three sequence.

<aside>
💡 Time complexity : `O(log⁡b(n))`. In my case that is `O(log⁡3n)`. The number of divisions is given by that logarithm.
Space complexity : `O(1)`. We are not using any additional memory.

</aside>
