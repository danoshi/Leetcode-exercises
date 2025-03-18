# 13. Roman to Integer

Let’s have a look on the description of the problem:

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

```
SymbolValue
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`.
Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

**Example 1:**

```
Input: s = "III"
Output: 3
Explanation: III = 3.
```

This problem seems at first glance really easy to achieve but the constraint with the subtractions make it more difficult than expected for me. Let’s have a look into my solution:

1. First we need to create a dict where we map the roman character to the actual value. Moreover, we create two helper variables, one for the total value and one to keep track of the length of our string.
2. Next we create a `while loop` with the condition to run so long until our helper variable is bigger then the length of the string.
3. In the `while loop` we need to check if our first element is smaller than the next one if this is the case we know that we need to subtract the next item with the current one and add the sum to our helper variable. After adding it to our total helper variable we need to add two to our helper variable which keeps track of the length of the string.
4. In the other case we just add the current index item to our total helper variable and after it, we add one to our helper variable which keeps track of the length of the string. In the end we return the total sum as an integer.

> As there is a finite set of roman numerals, the maximum number possible number can be `3999`, which in roman numerals is `MMMCMXCIX`. As such the time complexity is *`O*(1)`

> Because only a constant number of single-value variables are used, the space complexity is *`O*(1)`.
