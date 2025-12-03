# Get the Maximum Score — Two-Array Path Problem

This repository contains an efficient solution to the **"Get the Maximum Score"** problem, using a two-pointer technique to traverse two sorted arrays and compute the maximum possible path score.

---

## 🧩 Problem Statement

You are given two sorted arrays of distinct integers, `nums1` and `nums2`.

A **valid path** is constructed according to the following rules:

1. You start at index `0` of either `nums1` or `nums2`.
2. From there, you must traverse the chosen array from **left to right**.
3. Suppose you encounter a number that appears in **both arrays** (a common element, not necessarily at the same index). In that case, you may choose to **switch** to the other array at that element and continue the traversal from that point forward.
4. A common element can only be **counted once** in the total path score, regardless of the array in which it appears.
5. The **score** of a path is defined as the sum of all **unique elements** visited during traversal.
6. Your task is to return the **maximum possible score** achievable by any valid path.
7. As the answer may be too large, return the maximum score modulo **10^9 + 7**.

---

## 📏 Constraints

- `1 <= nums1.length, nums2.length <= 10^5`
- `1 <= nums1[i], nums2[i] <= 10^7`
- All elements in `nums1` and `nums2` are **strictly increasing**.

---

## 🔍 Key Insights

- Since both arrays are **strictly increasing**, there are no duplicates within a single array.
- Common elements act as **decision points** where you may switch from one array to the other.
- Between two common elements, you can only move forward in a single array, so you accumulate two partial sums: one for each array.
- At each common element, you add the **maximum** of these two partial sums (plus the common element) to the global total, ensuring that the common element is counted **only once**.
- After processing all shared intersections, you add the maximum of the remaining partial sums from the tails of both arrays.
- This leads to a clean, linear-time solution using a **two-pointer** approach.

---

## 🚀 Algorithm Overview

We use two pointers `i` and `j` to traverse `nums1` and `nums2`, respectively, along with two running partial sums `sum1` and `sum2`:

1. Initialize:
   - `i = j = 0`
   - `sum1 = sum2 = total = 0`

2. While either pointer is within bounds:
   - If `nums1[i] < nums2[j]`, add `nums1[i]` to `sum1` and move `i` forward.
   - Else if `nums2[j] < nums1[i]`, add `nums2[j]` to `sum2` and move `j` forward.
   - Else (we found a **common element**):
     - Let `val = nums1[i]` (which equals `nums2[j]`).
     - Add `val` to both `sum1` and `sum2`.
     - Add `max(sum1, sum2)` to `total`.
     - Reset `sum1 = sum2 = 0`.
     - Move both `i` and `j` forward.

3. After the loop, add `max(sum1, sum2)` to `total` to account for any remaining tail elements.

4. Return `total % (10**9 + 7)`.
   

---

## ⏱ Complexity

This algorithm runs in **O(n + m)** time and uses **O(1)** extra space (besides the input arrays).


