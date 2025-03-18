# 189. Rotate Array

The objective of this task was the following:

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

**Example 1:**

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```

My first solution was to create a `while loop` and in this loop create another `for loop` to go through every element and move it `k` times. This would eventually work out but for large arrays the time complexity would rise significantly since my Big O in this Solution would be `O(n²)` and because of that my solution in Leetcode was not accepted because I got a timeout in one of the test cases. \*\*\*\*

But still lets go step by step of what I did:

1. I created two variables, `length` which is the length of the array and `k` which adjust `k` to be within the range of the array length.
2. Now I create a `while loop` which checks if k is bigger than 0.
3. Now I store my last element of the array in a variable called temp.
4. In the next step I create a for loop which starts at the last element, stops when the index is 0 and goes backwards.
5. In this loop I set my current element `nums[i]` to the last element `nums[i -1]` . For example since I go backwards and my last item is 7, and we consider a sorted array my new `nums[i]` is now 6. We stored the last element before because now we shifted the array by one element but our last element 7 is now gone.
6. So after the loop finished we set `nums[0] to temp` which is 7. And in the last step we count k - 1 to do it k steps.

So I didn't think about the spatial or time complexity in the beginning, but in the future I will do that. So here comes a solution which someone in the Leetcode community posted and its only 2 lines of code.

```
k = k % len(nums)
nums[:] = nums[-k:] + nums[:-k]
```

This two lines solve the problem! Amazing, I was not thinking of slicing in the context of this problem. Let’s have a deeper look into the solution.

1. In the first line there is a `length` variable created which is called `k` and adjust `k` to be within the range of the array length.
2. Starting with `nums[:]` these assigns the concatenated result back to the original array `nums`.
   1. `nums[-k:]` this part slices the array from index `-k` which for example when `k` is 3 it would be the last three items in the array.
   2. `nums[:-k]` this part slices the array from the beginning of the array until the index `-k` , excluding the end of the array. So for example the beginning would include 0, but it would exclude the last element. If we take a list with a length of 7 and our k is 3. It would take `nums[0]` `nums[1]` `nums[2]` `nums[3]` but not `nums[4]` . You can calculate `nums[:-k]` following, length - k and exclude the last element.
