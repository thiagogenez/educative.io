# 📘 Create Maximum Number 

## 📝 Problem Statement

You are given two integer arrays **`nums1`** and **`nums2`**, of lengths `m` and `n`.   Each array represents the **digits of a number** (most significant digit first).

You are also given an integer **`k`**.

Your task is to **create the largest possible number of length `k`**, using digits from both arrays, while preserving the **relative order** of digits taken from the same array.

You may interleave digits from the two arrays in any way — but you **cannot reorder** digits *within* the original arrays.*

Your function must return the final number as a **list of digits**.

---

## ✔️ Constraints

- `1 ≤ m, n ≤ 500`
- `0 ≤ nums1[i], nums2[i] ≤ 9`
- `1 ≤ k ≤ m + n`
- No unnecessary leading zeros  
- Order within each array must be preserved  

---

## 🔍 Example

**Input:**
```
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
```

**Output:**
```
[9, 8, 6, 5, 3]
```

---

## 🚀 Algorithm Overview

This solution uses a **custom greedy upgrade strategy**, instead of the classical monotonic stack.

It has three main components:

---

## 🔹 1. `max_subsequence(nums, k)`
Extracts the lexicographically largest subsequence of length `k`.

### How it works:
1. Start with the first `k` digits.
2. For each next digit:
   - Try replacing each position in the current subsequence.
   - Keep the lexicographically best candidate.
3. Return the best subsequence found.

This uses Python's built-in lexicographical list comparison:
```
[6, 7] > [6, 0, 4] → True
```

---

## 🔹 2. `merge(a, b)`
Merges two digit sequences into the **largest lexicographically possible** result.

### Method:
At each step, compare the remaining suffixes:

```python
if a[i:] > b[j:]:
    pick from a
else:
    pick from b
```

This ensures we always choose the digit leading to the best possible final number.

Example:
```
a = [6, 7]
b = [6, 0, 4]

[6,7] > [6,0,4] → pick 6 from a
```

---

## 🔹 3. `max_number(nums1, nums2, k)`
Combines everything:

1. Try all valid splits of digits from nums1 and nums2.
2. Build subsequences using `max_subsequence`.
3. Merge using `merge`.
4. Track the lexicographically largest final sequence.

---

## 🧠 Complexity

Given the greedy-upgrade logic:

- `max_subsequence`:   Worst case: **O(k × (n - k))**

- `merge`:  **O(k)**

- `max_number`:  Tries at most **k** splits.

Overall practical complexity:    **O(k² × n)** which is safe for inputs up to 500 digits.

---

