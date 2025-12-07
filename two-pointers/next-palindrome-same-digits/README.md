# Next Palindrome by Digit Rearrangement

## Problem Description

You are given a **numeric string** `num_str` that **is already a palindrome**. Your task is to compute the **smallest palindrome strictly larger than `num_str`** that can be formed **using exactly the same digits**.

If no such palindrome exists, return an empty string `""`.

## Example

### **Input**

    123321

### **All palindromes using the same digits**

    213312
    231132
    312213
    132231
    321123

### **Output**

    132231

Because it is the **smallest** palindrome **greater than** `123321`.

## Constraints

-   `1 ≤ num_str.length ≤ 10^5`
-   `num_str` contains digits only
-   `num_str` is guaranteed to be a **palindrome**


## Solution Overview

A palindrome is determined completely by its **left half** (and middle digit if length is odd).

To find the **next larger palindrome**, the algorithm is:

1.  Extract:
    -   `left` = first half of the digits
    -   `middle` = the middle digit (if odd length)

2.  Compute the **next lexicographical permutation** of `left`.

3.  Mirror the new left half to form:

        left + middle + reversed(left)

4.  If `left` has no next permutation, no larger palindrome exists, therefore return `""`.

This works because increasing the left half to its next permutation produces the smallest possible overall palindrome greater than the original.


## Time Complexity

-   Extracting halves: **O(n)**
-   Next permutation: **O(n/2)**
-   Final reconstruction: **O(n)**

Overall complexity: **O(n)**\
Efficient for strings up to **100,000 digits**.


## Notes

-   This approach avoids generating all permutations.
-   Only the **left half** is permuted.
-   Guarantees the lexicographically smallest valid palindrome.

