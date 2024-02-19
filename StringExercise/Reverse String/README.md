# 344. Reverse String

Let’s have a look on the description of the problem:

Write a function that reverses a string. The input string is given as an array of characters `s`.

You must do this by modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) with `O(1)` extra memory.

**Example 1:**

```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```

In this problem we have the constraint that we are not able to use an additional array to store the values of the array. This constraint leads me to the conclusion that we would need `two pointers`. One is looking on the first item in the array and one on the last. They would `swap` so long until they find themselves in the middle. Let’s have a more detail look on the solution:

1. First I create `two pointers` called left and right, one is pointing to the `first element` which has the index 0 and the second one on the `last element` which is the length of the array minus one.
2. Now I created a while `loop` with the `condition` to run so long until left is bigger than right which would mean that they are in the middle.
3. In the loop I am swapping my left element with my right element and the right element is my new left element. After this is done I add up to the left index one and subtract from the right index one so that they come closer to each other.

Time complexity of this solution would be `Big O(n)` since we travers the array only once and even not fully since in the middle of it we stop. For the Space Complexity we are on `Big O(1)` since we did not use any additional space.

There is even a much easier solution to this, a one linear if you would think of it. 
We could just use the `built-in reverse function` from python, and it would as well solve it.