# 122. Best time to buy and sell stock II

**The objective of this task was the following:**

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

On each day, you may decide to buy and/or sell the stock. You can only hold **at most one** share of the stock at any time. However, you can buy it then immediately sell it on the **same day**.

Firstly when I was looking at the problem, I was again overthinking the solution. I defined helper variables with the name `buy`, `sell`, `total` and `helper` each of them had their purpose which was `buy` was defined with the value 0, and I would add it up when I bought something on a given day. `Sell` was also added up when I sold something. `Total` was the difference between `Sell` and `Buy` and last but not least `helper` was defined to keep track to not sell something when nothing was bought.

I am already making the solution more complex than it should be. In the next step I checked if the first value is 1 if yes I would buy it, so I set my `buy` variable to the value of `prices[p]` and set the `helper` variable to `1`, so that in the next iteration of the loop I would not buy. The next would be `if prices[p -1] < prices[p] and helper == 1 and sell > 0` which would be for the buy option, if the first element is not 1. As you can see this was much to complex and as well do not cover a lot of cases but, I was still going with this and trying to solve it which ended up in having more than 80 lines of code. At that moment I was solving one test case after another which was not the right was to go, so I started reading in the forum on how others approach this problem.

There I read something like this:

<aside>
💡 Since you can hold only 1 stock at a time. Just add up the differences between two consecutive days (if profitable).

</aside>

Before I trusted this sentence I did some calculations lets have a look: We start looking at the element on index 1 which is 1 and then look up the index before and see if our differences would be positive. 1 - 6 = -5 which is not profitable. Let's go to the next one. 3 - 1 = 2 this is a profitable day, so we save 2. 2 -3 = -1 which is not profitable. 4 -2 = 2 this is profitable, so we add 2 to our current 2 which = 4. Now we have 7 -4 which equals 3 which is again profitable and in total we have a profit of an amount of 7.

| 6   | 1   | 3   | 2   | 4   | 7   |
| --- | --- | --- | --- | --- | --- |

Now lets see if this is correct. The best buy would be at 1. After we would sell at 3 to make profit of 2. We would again buy at 2 and skip 4 to sell at 7 which would give us profit of 5. To add the profit which our first sell at 3 we would have a total profit of 7. So it is indeed the same profit as if we would just add up the differences for two consecutive days if profitable.

So lets convert this logic into a step by step coding guideline on how to do it.

1. First we need to define a variable which will save our profit. Moreover, a second variable is being created which stores the length of the prices array.
2. In the next step we loop through it in a range of 1 and the length of the array
3. Now in our if comparison we check if the element on our current index is greater than the index one before.
4. If this is the case then we calculate the current index element minus the element on the index before to get the profitable difference and add it up to our profit
5. Last but not least, just return the profit

It really comes to understanding the problem and finding the most efficient solution to a given problem.

The time complexity is O(n) since we only once go through the loop.
The space complexity is O(1) since we save the value in our variable.
