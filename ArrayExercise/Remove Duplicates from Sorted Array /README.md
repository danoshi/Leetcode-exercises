# 26. Remove Duplicates from Sorted Array

### Remove Duplicates from Sorted Array

The objective of this Leetcode problem was to remove the duplicated values from the Array. The array is sorted so duplicated values would go one by another.

My approach to this problem was the following:

1. First I created a helper variable called “`lastvalue`” and assigned it to None
2. In the next step I created an empty `array` where I would save the duplicated values in it. The reason why I would do this is that after I have all duplicated values in my empty array stored I could loop through it and call the remove method on my “`nums array`” to remove the duplicates. 
3. As next step I loop through the `Nums Array` and set the range to start with the index 1 (not 0) and go to the length of the array. 
4. After the loop I set an if condition which checks `if nums[n]` (my array on index n) is the same value `as my helper variable` “lastvalue” `or if nums[0]` (on index 0) is the same as `nums[n]` to check if the first value of the list is the same as second.
5. if the value is the same I append it to my empty array 
6. After the if condition is checked I update my lastvalue variable with the current value of the nums array, so I set it to `nums[n]`
7. Last but not least I loop through the helper array and call the `remove` function in the `nums` array to delete every element which is in the helper array.
8. In the end I return the length of the `nums array` to get the value how many unique items are in there.

This was my approach on how to tackle my “first” leetcode problem. In the end it took my quite a while until I got it correct, but I am happy that I could solve it without searching for help in the internet or using AI. 

Let's have a look on the Leetcode solution how they did it:

There solution is quite easier and when I saw it first I had the feeling that I over-engineered or was thinking to complex but nevertheless, lets break down the leetcode solution to get a better understanding.

 

1. They created to helper variables one is called “`size`” which has the value of the length of the nums array and the second variable is “`insertIndex`” which is set to 1.
2. In the next step we create a loop where we loop through the nums array in the range of starting by 1 and the ending point would be the variable size, since this variable has the length of the array. 
3. Now the interesting part comes in: What they did is they created an if condition (`nums[i - 1] ! = nums[i]`) which is checking the value of `nums[i - 1]` which is the first value of the array because we started at 1 and arrays are indexed with 0 and `nums[i]` which is the first value according to our starting position from the range in the loop. 
4. If the condition is `True` we found a unique value, so we update our array on that position, we set the `nums[insertIndex] = nums[i]`. Afterward we increment the insertIndex by one since the list is order the next value can only be one higher.
5. The last step is to return the `insertIndex` since this value will tell us how many unique items the array will have.

As you can see the Leetcode solution is much shorter in steps and keeping it to the point. When I am looking at it, it seems obvious but when I sit down solving the problem I would probably never come up with this. In the end it comes to the point on how much do you practice daily and how much effort do you put into coding and understanding on what you do. With, time it will definitely get easier so keep on going.