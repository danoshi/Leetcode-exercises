# Two Sum

## Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

## Solution Approach

We use a hash map to store previously seen numbers and their indices. For each number, we:

1. Calculate the complement (target - current number)
2. Check if the complement exists in our hash map
3. If found, return both indices
4. If not, add current number and index to hash map

## Complexity Analysis

- Time Complexity: O(n)
- Space Complexity: O(n)

## Code Implementation

```python
def two_sum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```
