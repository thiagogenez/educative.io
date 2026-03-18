# Remove Element (In-Place)

## Problem Statement

You are given an integer array `nums` and an integer `val`.

Your task is to remove all occurrences of `val` **in-place**, meaning: -
You must not allocate extra memory for another array - You can modify
the input array directly

After removing the elements, return the number of elements that are
**not equal to `val`**.

------------------------------------------------------------------------

## Requirements

Let `k` be the number of elements in `nums` that are not equal to `val`.

Your solution must ensure:

-   The first `k` elements of `nums` contain values **not equal to
    `val`**
-   The order of elements **does NOT matter**
-   Elements beyond index `k` are irrelevant

------------------------------------------------------------------------

## Example

``` python
nums = [3, 2, 2, 3]
val = 3
```

Output:

    2

Modified `nums` (first k elements):

    [2, 2, _, _]

------------------------------------------------------------------------

## Approach

This solution uses a **two-pointer technique**:

-   `i` starts from the beginning
-   `k` starts from the end
-   If `nums[i] == val`, swap it with `nums[k]`
-   Decrease `k` to shrink the valid range
-   Continue until pointers meet

------------------------------------------------------------------------

## Implementation

``` python
def removeElement(nums, val):
    i = 0
    k = len(nums) - 1

    while i <= k:
        if nums[k] == val:
            k -= 1
            continue

        if nums[i] == val:
            nums[i], nums[k] = nums[k], nums[i]
            k -= 1

        i += 1

    return k + 1
```

------------------------------------------------------------------------

## Complexity Analysis

-   Time: O(n)
-   Space: O(1)

------------------------------------------------------------------------

## 🧠 Alternative Approach (Overwrite Method)

``` python
def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
```

------------------------------------------------------------------------

## Edge Cases

-   Empty array → return `0`
-   All elements equal to `val` → return `0`
-   No elements equal to `val` → return `len(nums)`

------------------------------------------------------------------------

## Summary

-   In-place modification is required
-   Order does not matter
-   Two-pointer solution is efficient
-   Overwrite method is simpler and commonly used
