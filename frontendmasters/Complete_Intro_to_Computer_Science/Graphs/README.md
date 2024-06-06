## Graphs

Graphs are a datastructure that is extremely useful, but you may not use it in your code daily. They are all about modeling relations between many items. In comparison to trees, here we do not have a structure with left and right subtrees. In Graphs the connections are one to many or many to many or even one to one. An example would be Facebook. In Facebook each person would be a node which could be compared to and SQL row in a database. Next we would have “friendships” between nodes which are edges. The edge would represent the connection between the two nodes. In Facebook the connection is bidirectional since one sends the friendship request and the other one have to approve or accept it. In X or former Twitter we have unidirectional edges since there someone can just follow me and I do not need to follow back or approve it per default.

Let’s have a look on a basic graph and use an algorithm to find the most common job title amongst the people I follow:

```plaintext
   Peter — Dan
  /    \
me    Aleks
  \    /
   Eva
-> Add me to queue
-> Dequeue me
-> Add my job to the tally (devops)
-> Queue my connections, Peter and Eva
-> Dequeue Peter
-> Add Peter's job to the tally (frontend)
-> Queue Peter's connection, Dan and Aleks
-> Dequeue Eva
-> Add Eva's job to the tally (architekt)
-> Queue Eva'S connections. Aleks has already been queued so don't add any.

-> Finish first iteration, one degree of separation
```

> So traversing algorithm fits best here? We're analyzing everything in a limited depth of a sub-tree and breadth-first is well-equipped to do that. Instead of letting breadth-first traversal run to completion, we'll just limit how many times that outer loop runs, effectively limiting how many levels down it goes, or how many degrees of separation!
>
