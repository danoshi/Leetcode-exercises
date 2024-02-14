### Quick Sort

Quick Sort is as well a recursive algorithm, but it takes a different approach than Merge Sort. 
You define a `pivot` which is usually the last item in the array, and then you start comparing, everything bigger than the pivot will get into the right arrays, everything smaller than the pivot will go to the left array. 

> The base case is when you have a list of length 1 or 0, where you just return the list given to you.
>

As we can see in the example we take 4 as the `pivot` and start comparing.

5, 9, 5, 8, 7 are in the right aray since they are bigger

3, 2, 1 are in the left array since they are smaller

> You then call quick sort on the left and right lists independently (hence the recursion.) After those two sorts come back, you concatenate the sorted left list, the pivot, and then the right list (in that order.)
> 

The worst case scenario for quick sort would be a sorted list, since the last item would be the biggest and everything would be in the left array. This would lead to a `O(n²)` . Same would apply to a reverse order list since there everything would be in the right array.

The best / average case would be a randomly sorted list. Here we would have a Big O of `O(n log n)` .

> What about spatial complexity? In the way that I'm going to have you do it, it'll be `O(n)`.
> 