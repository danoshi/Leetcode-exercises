# 1051. Height Checker

A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in **non-decreasing order** by height. Let this ordering be represented by the integer array `expected` where `expected[i]` is the expected height of the `ith` student in line.

You are given an integer array `heights` representing the **current order** that the students are standing in. Each `heights[i]` is the height of the `ith` student in line (**0-indexed**).

Return *the **number of indices** where* `heights[i] != expected[i]`.

**Example 1:**

```
Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation:
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.

```

**Example 2:**

```
Input: heights = [5,1,2,3,4]
Output: 5
Explanation:
heights:  [5,1,2,3,4]
expected: [1,2,3,4,5]
All indices do not match.
```

In this problem we need to check if the `array` which we get as an input is `sorted` and if not return the `count` of `elements` which are not in order. Let’s have a look into my solution:

1. I first initialize two variables which both are set to zero. One will be counting the elements in the array and the other are counting the elements which are not in order.
2. In the next step I create a shallow copy of the current `heights` array so that I can sort the copied array. For this I used the `copy()` method which creates a shallow copy which saves memory since a new object is created which has references to the old one. Now I have an array called `sorted` , on this array I call the `sort()` method to have the array sorted.
3. Now I create a `while` loop which runs so long until I went through all elements in the array.
4. In the `body` of the `loop` I have an if statement which check whenever an element from the sorting array is not equal from the original array. If this is the case we add one to the `counter`. In the end we add up the `index` to check the next element.
5. Last but not least we return the `counter` which tells me how many elements are not sorted in my original array.

**Big O**

- Time Complexity: `Big O(n)`, where `n` is the number of elements in the array.
- Space Complexity: `Big O(1)` . I did not use any additional space.
