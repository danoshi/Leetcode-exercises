# 66. Plus One

Let's have a look on the description of the problem:

You are given a **large integer** represented as an integer array `digits`, where each `digits[i]` is the `ith`
 digit of the integer. The digits are ordered from most significant to 
least, significant in left-to-right order. The large integer does not 
contain any leading `0`'s.

Increment the large integer by one and return *the resulting array of digits*.

**Example 1:**

```
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
```

My Big O in this time is `O(n)` and the space complexity is constant since I am not using additional arrays. Let's have a look on how I approached this issue.

1. Basically there are three main cases which are:
    1. My last item in the array is smaller than 9
    2. My last item in the array is 9 and the next one is smaller than 9 
    3. My last item in the array is equal to 9 and the next one is 9.
2. I started to implement the easiest case which is my last item is smaller than 9. So I started with creating a variable with the actual length of the array and then in an if condition to check if it's smaller than 9, if yes just add to the last item in the array one and return the array
3. If this is not the case we need to loop through the array in a reversed order to start from the last item and in a range of the length of the array plus one to handle the edge case if there is only one item in the array.
4. in the loop now I check if my item is smaller than one, if yes I just add to the next number plus one and return the array. If this is not the case I set the current item to 0 since. If my array consist only from nines I would have in the end only zeros and because of that I add after the loop at index 0 the number 1 and return the array.

It is really important to think of all the cases which could happened and then implement one by one. In the end there is always time to make the code more readable or adjust it.