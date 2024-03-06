## Radix Sort

Radix sort is a non-comparison based sorting. 

We're going to sort the ones place first, so all the numbers in the ones place are in order from 0 to 9. We will create ten buckets, one for each integer zero to nine. Then we'll loop `d` times when `d` is the maximum length of a number in our array. So if the longest number in our array is 90932 then `d` would be 5. Then in the inner loop we would enqueue all the numbers in the buckets based on what digit we were sorting and then dequeue them back into the main array.

Big O here is different from in the other search algorithms since you are dependent on another `variable` which is d in our example and that is the maximum length of a number. 

> The more buckets we need, the larger the complexity. So instead of being O(n²) or O(n _ n), it ends up being O(n _ k). So is it better or worse than O(n log n) sorts? It depends! If you have a lot of numbers with lots of varied lengths that will bucket into a good distribution it can be very effective. If you number [1, 10, 100, 1000, 10000, 100000] etc. it ends up being the worst sort. It ends up being O(n²) at that point.
> 

> What about the spatial complexity? It ends up being O(n + k) and this why radix sort is really only used in very specific circumstances: it's not great in terms of how much space it takes.
> 