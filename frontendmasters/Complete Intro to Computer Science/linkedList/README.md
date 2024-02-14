## LinkedList

For our second data structure, we're going to implement a LinkedList. LinkedList is made of a bunch of nodes that point to the next one in the list. Every node in a LinkedLists has two properties, the value of whatever is being store and a pointer to the next node in the list. These nodes will not be sequential in memory, meaning we don't get the easy lookups but the advantage is that adding things is easy since we don't have to do the compacting we had to do with ArrayList.

So let's talk about look-ups. You only have access to a head node. The head node will point to the 1 node. The 1 node points to the 2 node, etc. If we want to lookup index 10,000 we're going to have to make 10,000 jumps. That means the lookups grow with length and therefore the Big O is O(n) for lookups.

Let's chat about where LinkedLists are useful then. What do we need to do if we want to delete index 10? We'll first do a lookup node 9, and we'll change the pointer of node 9's to point at node 11. Done! So these deletions are O(1).