## Tries

Trie is a specific tree data structure which is optimized for searching by prefix. The most common example which everyone is familiar is autocompletion. A trie starts with a root node that doesn’t represent anything. Often it is just an empty string.

> It has a bunch of child nodes (as many are necessary) that represent one letter, the first letter of all the words added to the data structure. Each of those letter-nodes will have children nodes for all the *second* letters of the words that are represented in the data structure. So on and so forth, there will be a chain of nodes that represent each letter in the data structure.

Below an example of how this data structure looks like:

```plaintext
  a – [various children]
 /
b – o – s – t – o – n
     \
      i – s – e
```

> So based on this, you'd get suggestions of "Boston" and "Boise".
>
> Since some words are contained within chains of others (for example, there are two separate cities, one called "Salina" and one called "Salinas" or "Sandy" and "Sandy Springs".) You'll often have a flag in there that signifies the node you're on is a complete word, so you can just add it to the list and then keep going on the children.
