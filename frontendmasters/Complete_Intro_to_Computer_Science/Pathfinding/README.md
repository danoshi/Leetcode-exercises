## Pathfinding

Since we are aware of data structures like trees or graphs there is an interesting concept called **Pathfinding**. Let’s imagine there is a Grid, and we have some coordinates from point A and some coordinates from point B. Now we need to find a way how A can reach B.

```plaintext
• • • • •
• A • • •
• • • • •
• • • • •
• • B • •
```

Looking at the example above we would have many different option, we could go down from A until we reach the last row and then move right until we reach B. Another way would be to go one step to the right and then move down until we find B. Both of them would count as the **shortest path** to B.

In the example above we do not have any constraints but what would happen if between A and B would be a wall?

```plaintext
• • • • •
• A • • •
• • • • •
• X X X X
• • B • •
```

Now our algorithm would not work anymore. Here, the basic idea of the Dijkstra algorithm comes in. In this algorithm, we start at both places—the beginning and end node. We start “spiraling” outwards, marking each node with how far away it is from its original node.

Below how it would look like after the first iteration at point A:

```plaintext
• 1 • • •
1 A 1 • •
• 1 • • •
• X X X X
• • B • •
```

Now we do the same but for point B:

```plaintext
• 1 • • •
1 A 1 • •
• 1 • • •
• X X X X
• 1 B 1 •
```

We will do this exercise until we intersect with the two spirals. As soon as the spiral intersect we know we’ve found the shortest possible path.

```plaintext
2 1 2 • •
1 A 1 • •
2 1 2 • •
• X X X X
• 1 B 1 •

2 1 2 • •
1 A 1 • •
2 1 2 • •
• X X X X
2 1 B 1 2

2 1 2 3 •
1 A 1 2 3
2 1 2 3 •
3 X X X X
2 1 B 1 2

# We now intersect with B
```
