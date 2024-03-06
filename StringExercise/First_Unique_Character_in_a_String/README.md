# 387. First Unique Character in a String

Let’s have a look on the description of the problem:

Given a string `s`, *find the first non-repeating character in it and return its index*. If it does not exist, return `-1`.

**Example 1:**

```
Input: s = "leetcode"
Output: 0
```

In this problem I used more built-in Python stuff which was new for me, but I learned a lot out of it. Let’s have a more detailed look on it:

1. I defined a counter variable which is using the `Counter Python Object`. Counter counts the occurrences of each character in the string. This line creates a dictionary-like object where the keys are the characters in the string and the values are their respective counts. 
2. Now we create a for loop, but we use the `enumerate()` function to get both the character and its index in the string. We use the `enumerate()` function because our counter variable is a dict so a key value store, so we need to check the index of the string character. 
3. In my `for loop` I have an if condition which checks if the value of the current dict element is 1 which would mean that the letter of the string is unique since it only occur once. If this is the case we return the index of this element, if not we return -1. 

> Time complexity: `O(N)` since we go through the string of length `**N**` two times.
> 
> 
> Space complexity: `O(1)` because English alphabet contains 26 letters.
>