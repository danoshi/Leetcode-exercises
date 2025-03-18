# 242. Valid Anagram

Let’s have a look on the description of the problem:

Given two strings `s` and `t`, return `true` _if_ `t` _is an anagram of_ `s`_, and_ `false` _otherwise_.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**

```
Input: s = "anagram", t = "nagaram"
Output: true
```

In this problem we need to check if the two inputs which we get are a valid anagram. My approach of it was just adding both words in separate arrays, sort them and if they are equal we would return `True` otherwise `False` . Let’s have a more detailed look into my solution:

1. As mentioned before in the first step I create two empty arrays.
2. In the next step I create two `for loops` which are not nested, in the first loop I loop through the first word and append every letter to one of the array. In the second loop I loop through the second word and append it to the array. Now I have in the two arrays every letter of the two words.
3. Now I just call the built-in method of python `sort()` on both of the arrays. This is needed because if the word is an anagram sorting it will be in the correct order and would have the letters on the same index.
4. In the end I just have an if condition, if array one is the same as array 2 and if so, I would return `True` otherwise `False`.

The time complexity here is `Big O(n)` and space complexity is as well `Big O(n)`.
