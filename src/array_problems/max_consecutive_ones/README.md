# 485. Max Consecutive Ones

Let’s have a look on the description of the problem:

Given a binary array `nums`, return _the maximum number of consecutive_ `1`_'s in the array_.

**Example 1:**

```
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
```

This problem seems at first not that difficult since we could just loop through the array set a counter and add the counter up and set it to 0 if we have a 0, and this would work perfectly fine for the example above but what if we would have the reversed array? Our counter would be two and not three so here we need modify our approach to the problem a little bit. Let’s have a look in a more detail into my solution:

1. At first, I initialize one helper variable called counter and empty array. In counter variable I will add up whenever one appears in the array and set it again to zero if zero appears in the array. The array is needed to store the value of the counter when a zero occurs before setting it to zero themselves.
2. Now we just `for loop` through the whole array to start the counting.
3. In the `for loop` we create some conditions, first we check if our current element is one, if yes we count our counter plus one. However, when our current element is not one we add our current counter value to the array and in the next step we set the counter to zero.
4. After the `for loop` we append again the counter to the array because it could be that the array only consist of one’s, so it would only count up. In the next step we use the pythons built-in function `sort()` to have the biggest number at the last index in our array.
5. In the end we return the last index of our array which is the number with the maximum of _consecutive_ `1`_'s in the array._

Time Complexity: `Big O(n)`, where `n` is the number of elements in the array.
Space Complexity: `Big O(n)` . I use an additional array.
