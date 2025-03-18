# 1346. Check If N and Its Double Exist

Let’s have a look on the description of the problem:

Given an array `arr` of integers, check if there exist two indices `i` and `j` such that :

- `i != j`
- `0 <= i, j < arr.length`
- `arr[i] == 2 * arr[j]`

**Example 1:**

```
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
```

In this problem there is an edge case which you probably faced but depending on your solution it could also be that your implementation already covered it. For me, it was not the case, so let's have a more detailed look into my solution:

1. I created two variables, one named counter which I set to zero, and the other one I called length which has the value the length of the array.
2. Now I create another variable called count and here I use the `python package collections` to use the function `Counter`. The function is counting the occurrences of a value in an array and store it as a `key value hashmap`. I used it for the edge case which is `0`. Later on I will explain why.
3. Now before I create any loop I have an `if condition` which checks if my count variable has two or more `0` in it. If yes we immediately return `True` .
4. If there is no `0` value in the array which is passed to the function we go to the next step which is the `loop` . Here I have the while loop which is running so long until the counter is smaller than the length of the array. In the loop I created another for loop. In there I calculated from the first array the sum of the multiplication with 2 and check with all the elements if there is an element which has the same sum. If yes we return `True` , if not we add one to the counter and for loop it again with all elements.
5. Now the edge case would be if there is an `0` in the array since the sum of `2 * 0` is `0` so, in the for loop it would return True for the same element which we did the calculation, so I enhanced my if to check as well if my current value from the array is not `0` . Even if there would be multiple `0` in the array the first if condition is covering this case so here we would simply don’t care about it.
6. If the loop finishes, and we still would not find any element we would simply return `False`.

Time Complexity: `Big O(n²)`, where `n` is the number of elements in the array.
Space Complexity: `Big O(1)` . I did not use any additional space.
