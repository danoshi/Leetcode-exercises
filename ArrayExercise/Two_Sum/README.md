# 1. Two Sum

Let’s have a look on the description of the problem:

Given an array of integers `nums` and an integer `target`, return *indices of the two numbers such that they add up to `target`*.

You may assume that each input would have ***exactly* one solution**, and you may not use the *same* element twice.

You can return the answer in any order.

**Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

My approach to the Solution was the following, since we need to add up two numbers in our Array which are the target it would be the easiest to create a `for loop` and just check the current element and the next one if they add up the sum. This would probably work for most of the solutions but what if the first and the last element will in total give us the target. This would be not covered by a simple `for loop` . We would need to run the for loop and check the first element with every other element if the first one in addition if any other results in the sum. Let’s have a more detail look on my approach:

1. Firstly I create a new array where I want to store the indexes of the numbers which result in the sum. In addition, I define two variables which have the value of the length of the array.
2. Next I create a `while loop` where I have the condition k (which is the length of my array) is smaller than 0. 
3. Now in the `while loop` I have a for loop which and in this for loop I have an if condition which check now every element of index `n` where `n` my index of the `for loop` is and `k` the current element so the first one will be checked with every other if in total both result in the target. If yes I append both elements to my array and return it. If not I calculated `-1` to my `k` and run the for loop again.

My solution has a time complexity of Big `0(n²)` and space complexity of constant since I just have one array and add up always two numbers into it. 

There is even the possibility to do this with a time complexity of Big `O(n)` , this solution includes a hashmap and a for loop. 

1. First we create an empty Hashmap.
2. Next we iterate through it and set a variable called complement. This variable results in `target - nums[i]` 
3. Now we check if the result of the calculation is already in our hashmap, if yes we return the current value of the loop the variable so called `i` and the value on the index `hashmap[complement]` . If not we add the value to our hashmap on the current index. 

With this solution we have only Big `O(n)`. 

> We traverse the list containing nnn elements only once. Each lookup in the table costs only `O(1)` time.
> 

```
def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i
```