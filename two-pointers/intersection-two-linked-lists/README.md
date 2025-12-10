# 📘 Intersection of Two Linked Lists

## 📝 Problem Statement

You are given the **heads of two singly linked lists**, `headA` and `headB`.   Your task is to **determine whether the two linked lists intersect**.

If an intersection exists, return the **node where the intersection begins**.   If they do **not** intersect, return `None`.

> ⚠️ **Important:**  
> Two linked lists intersect **only if they share the exact same node in memory**. Having equal values (`node.val`) does **not** mean they intersect.

---

## 💡 Example

```
List A: 1 → 2 → 8 → 9
                ↑
List B:   3 → 4 ┘
```

Both lists share node **8**, so the intersection begins at the node with value `8`.

---

## 📚 Constraints

- Node values:  
  `1 ≤ node.val ≤ 10^5`
- Number of nodes:  
  `1 ≤ m, n ≤ 10^3`
- Lists may be of **different lengths**
- Intersection occurs only if the two lists share **the same memory reference**

---

## 🚀 Approach (Two-Pointer Switching Technique)

We use a pointer technique with **O(1) space**:

1. Initialize:
   - `ptrA = headA`
   - `ptrB = headB`
2. Traverse both lists simultaneously.
3. When a pointer reaches the end, redirect it to the **other list’s head**.
4. Eventually:
   - If the lists intersect, then both pointers meet on the intersection node.
   - If not, both pointers reach `None` at the same time (therefore, intersection)

### ✔ Why this works

Both pointers traverse exactly:

```
len(A) + len(B)
```

Thus, they align regardless of the initial length difference.

---

## ⏱ Time & Space Complexity

| Complexity | Value      |
| ---------- | ---------- |
| **Time**   | `O(m + n)` |
| **Space**  | `O(1)`     |

This is optimal for this problem.
