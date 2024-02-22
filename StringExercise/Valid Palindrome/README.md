# 125. Valid Palindrome

Let’s have a look on the description of the problem:

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` *if it is a **palindrome**, or* `false` *otherwise*.

**Example 1:**

```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

In this problem we need to check the `string` if it is a Palindrome, which means the string needs to be the same as reversed and not reversed. For that problem we need two pointers because we need to look on the first index of the string and the second one will look on the last index and what we basically do it we compare the first index which the last one if there are the same we add to the first index one and to the last index the subtract one. We do this process until we are in the middle of it and if all the characters are the same we know it's a Palindrome since we could switch them and still the same would be the outcome. Let’s have a more detailed look on my solution:

1. First we create two pointers, one has the value zero since it will have a look on our first index and the second one will have the value length of the array minus one to get the actual last index.
2. Now we create a `while loop` which will run so long until our first pointer which is looking on the first index is bigger then the second pointer which is looking on our last index. 
3. In this while we have to create the two additional `while loops` to check if the current character is an alphabetical character, if it is we just skip it and add to the index one more and to the second pointer the subtract one. 
4. If one of the elements is not same for both counter we stop the loop and return `false`  if our loop finishes we return `true` since all the characters are the same.

This solution has time complexity of `Big O(n)` where n the length of the string is. There is no additional space needed so the space complexity would be `Big O(1)`.