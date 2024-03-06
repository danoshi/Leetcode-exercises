# 217. Contains Duplicate

The objective of this problem is following:

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

**Example 1:**

```
Input: nums = [1,2,3,1]
Output: true
```

Basically my approach was again a Big `O(n²)` which eventually at one test case got time exceeded. But I would still like to showcase on how I approach this problem.

1. Since we have to check whether an array contains a duplicate value we would need to check it `n` times when `n` our length of an array is.
2. So I create a variable with the length of the array minus one to get the actual length. A second variable `counter` which is the length of the array without the minus one.
3. Now we want to check all items which each other, so I created a while loop which has the condition to run so long until my `counter`  is greater or equal to 0. Inside the while loop I have a for loop and in this for loop I created a `temp` variable which is set to the last element of the array. 
4. Last but not least I created within the for loop an if condition which checks if the last item of the loop is equal to one of the others.
5. When the for loop finish I subtract 1 from the index of my `temp` variable and 1 from my `counter` 
6. With this approach I check every item with everyone and if a duplicate is found I return `True` otherwise `False`

With this approach I have a huge time complexity, but it is a solution.

However, there is a solution which has only Big O of `O(n)` which would be linear time complexity. Let's have a look on that one.

What is important is not to forget about the built-in methods which could help by solving the issue. In this particular use case we want to see duplicated items, so if the array would be sorted my next item would be the duplicate, if there is one.

1. With the information above what we can do is we create again one variable called `length` and assign it the actual length of the array. 
2. Now we do `nums.sort()` and with this one we have a sorted array. 
3. In the next step we only need to loop through the array and in the if create a condition to check if my current item is equal to my next item and returning True or False

Basically again every problem can be solved in different ways. Just don’t forget to optimize your solution whenever possible but first make it work!