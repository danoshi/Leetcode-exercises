# 350. Intersection of Two Arrays II

Let's have a look on the description of the problem:
Given two integer arrays `nums1` and `nums2`, return *an array of their intersection*. Each element in the result must appear as many times as it shows in both arrays, and you may return the result in **any order**.

**Example 1:**

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
```

My Solution is again Big O of `O(n²)` but as I mentioned earlier solved, is solved and optimizing comes later. Let's have a look on have I approached the problem.

1. We need to create a new array which we return in the end with all the unique items. 
2. Next what I thought is that to have a list of unique items I need to check every item with everyone. So I create nested for loops, the first one loops through the first array and in that for loop I loop through the second one.
3. Now I can compare every element from loop one with every item from loop two. 
4. In my second for loop I created an if condition which checks if the elements are the same and if they are here the most important part is. We add the element to the new array, delete it from the inner loop since it already is added and break the inner loop, so that the outer loop can take the next element.

It is easy to read and to understand but not efficient if working with larger arrays.