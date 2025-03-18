## Binary Search

Search is the act of looking for a particular element in an array. This ends up being really similar to sorting, just instead of doing a whole array, we're just looking for one element in an array.

There are essentially two common ways of doing search: linear search and binary search. The former is the simplest code and really only useful if the list you're searching on is not sorted in any way. You just go through from 0 to the length of the array and ask "is this the element I'm looking for?" No frills here. Its complexity is `O(n)`.

Binary search is a bit more interesting. **It only works if the array is already sorted.**
For example, you search for 12, so you will go to the middle of the array which is 19 and start checking, is 12 bigger or equal to 19? No it's not bigger, so I need to go to the left side. So I do the next check, is 12 bigger or equal to 15? No it's not bigger I need to go more to the left side. Finally, we ask again is 12 bigger or equal to 12? Yes, now I have my element.

`[0, 5, 10, 12, 15, 19, 21, 22, 24, 30]`
