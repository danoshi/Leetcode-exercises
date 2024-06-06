## Bloom Filters

Bloom filters are an interesting data structure which are designed to tell you quickly and efficiently if an item is in a set. The trade-off which they are taken is following, they can’t tell you for sure if an item is in the set, but they can definitely tell you that an item is not part of the set. Stated differently, bloom filters have a false positive rate but do not have false negatives.

The website **Medium** is using the data structure of bloom filters in a way that after you read an article on their website you will get three recommendations below, which are for sure articles which you have never read before.
