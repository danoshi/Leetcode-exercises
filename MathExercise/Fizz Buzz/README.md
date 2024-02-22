# 412. Fizz Buzz

Let’s have a look on the description of the problem:

Given an integer `n`, return *a string array* `answer` *(**1-indexed**) where*:

- `answer[i] == "FizzBuzz"` if `i` is divisible by `3` and `5`.
- `answer[i] == "Fizz"` if `i` is divisible by `3`.
- `answer[i] == "Buzz"` if `i` is divisible by `5`.
- `answer[i] == i` (as a string) if none of the above conditions are true.

**Example 1:**

```
Input: n = 3
Output: ["1","2","Fizz"]
```

In this problem we get already hints in the description, one of the hints is that we need multiple if statements to check the different conditions. To check all of these conditions we need to loop through the integer `n` or loop so long as the integer `n` is. Let’s have a more detailed look on my solution:

1. First I created a new array where I would store my response. Additionally, I created a helper variable counter which I set to one, since we start with one.
2. In the next step I created a `while loop` with the condition to run as long as my counter is less than equal then my `n` . 
3. Now we write our if statements which checks the different cases when to append “FizzBuzz”, “Fizz”, “Buzz” or the counter as `string` in our results list.
4. After all the if conditions are done we add one to our counter to check the next number. After the `while loop` finished we return our results list.

The time complexity of my solution is `Big O(n)` since we loop so long until our n value and for the space complexity of my solution is as well `Big O(n)` since we created an additional array to append the result of the calculations.