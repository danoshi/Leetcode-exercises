## Recursion

What recursion does is, it breaks large, difficult-to-solve problem s into multiple smaller problems and try to solve this first. In the end all the small solved problems are put together so that the big problem is being solved with the help of the smaller ones. 

In programming a recursive function is a function that calls itself. 

```
def countTo(self, maximum, current):
	if current > max:
		return
	return countTo(maximum, current + 1)

print(countTo(5, 1))
# this would print counting to 5 and starting from 1
```

As we see in the last example it's not that useful for counting since the above solution is more memory intensive than a for loop.

But a use case for recursion would be fibonacci. A fibonacci number is the sum of the previous two fibonacci numbers. That being said `fibonacci(3)` is equal to `fibonacci(2) + fibonacci(1)`. To generalize this, `fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)`. This is a recursively defined problem.

The first question which we have to ask ourselves in recursion is what is the `base case`.
The `base case` is when we stop recursion. If we don’t define a `base case` we will most probably get a stack overflow when we run out of memory.

> *Almost always* with recursion your base case will be the first line of your recursive function. You need a good reason for that not to 
be the case.
> 

```
def fibonacci(n):
	# base case
	if n == 2 or n == 1:
		return 1
	elif n <= 0:
		return 0
	return fibonacci(n - 1) + fibonacci(n - 2)
```


What fibonacci is doing in the background is just adding 1 multiple times to each self. For fibonacci(6) for example we add up one, eight times because fibonacci(5) is 5 and fibonacci(4) is 3 so in total this is eight. 

The code itself is really elegant since its easy to read, but it is not really efficient since in a for loop this would be much faster, but again depending on the use case recursion can be more suitable than other solutions. 
