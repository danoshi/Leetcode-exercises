# 1299. Replace Elements with Greatest Element on Right Side

Given an array `arr`, replace every element in that array with the greatest element among the elements to its right, and replace the last element with `-1`.

After doing so, return the array.

**Example 1:**

```
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation:
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

```

**Example 2:**

```
Input: arr = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.
```

When we're looking at this specific problem we can see that what we need to do it taking the first element of the `array`, excluding it from the `array` and then searching in the `array` for the `max` value of the items which are left. Now that we have the greatest element from index 1 until 5 we can set the greatest element to be our 0 element in the array. Now we do the same for the element two. We exclude the first element which we already set and as well the second one. Now we search for the greatest element between 2 and 5. We do this until our last element, since the last element has no neighbour we set it to `-1` . This solution would have a Big O of `O(n²)` which is not as suitable as we would like to. Let’s have a look on a solution which do this differently:

1. First we initialize two variables in our code. One will store the actual length of the array and the other one the right Maximum which is `-1` since our last element will be always `-1`.
2. Now we loop through the array, but we start with the last item, go always one step back and end the loop when we are at the first item of the array.
3. As a next step we create a new variable called new Maximum which uses the Math operation `Max` and takes the right Maximum which is currently `-1` and the current element of the array.
4. After this step we can set our current element to the right Maximum because our last element in the array has no neighbour, so it has to be -1.
5. Last but not least we set the right Maximum value to have the value of our new Maximum so that the next element has the correct `max`.
6. Now we can return the in place modified array.

**Big O**

- Time Complexity: `Big O(n)`, where `n` is the number of elements in the array.
- Space Complexity: `Big O(1)` . I did not use any additional space.
