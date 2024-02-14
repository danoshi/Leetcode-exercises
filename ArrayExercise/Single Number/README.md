# 136. Single Number

Let's have a look on the description of the problem:

Given a **non-empty** array of integers `nums`, every element appears *twice* except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

**Example 1:**

```
Input: nums = [2,2,1]
Output: 1
```

Here again we can take the built-in functions from python as helping hands to solve the issue. What is important we can only use Big `O(n)` and use constant space which would be only one additional array. 

1. As, first we create a new array where we would store our unique values.
2. Now we iterate through the array of nums.
3. In the for loop we have an if condition which check if our first value from the list is not available in our unique values list. So the first item is not in our unique list since the list is empty, so we add it in there.
4. Now we go with the next item, if this item is in our list we go to the else block and remove the item, so our list is again empty. We are doing this with every element in the nums array so eventually only the unique one will be left.
5. In the end when the unique one is left we use pop() to return it.