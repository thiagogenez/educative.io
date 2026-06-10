# Count Subarrays With Fixed Bounds

## Problem Statement

You are given an integer array `nums` and two integers `minK` and `maxK`.

Return the number of **fixed-bound subarrays**.

A subarray of `nums` is a **fixed-bound subarray** if it satisfies **both**
of the following:

- The smallest value in the subarray equals `minK`
- The largest value in the subarray equals `maxK`

A subarray is a **contiguous** sequence of elements within the array.

------------------------------------------------------------------------

## Constraints

- `2 <= nums.length <= 10^3`
- `1 <= nums[i], minK, maxK <= 10^3`

------------------------------------------------------------------------

## Example

``` python
nums = [1, 3, 5, 2, 7, 5]
minK = 1
maxK = 5
```

Output:

    2

The fixed-bound subarrays are `[1, 3, 5]` and `[1, 3, 5, 2]`. Each has a
minimum of `1` and a maximum of `5`. The `7` cannot be part of any valid
subarray because it exceeds `maxK`.

------------------------------------------------------------------------

## Approach

The solution counts, for each index `i`, how many valid subarrays **end**
at `i`. It tracks three positions while scanning once from left to right:

| Variable   | Meaning                                              |
| ---------- | ---------------------------------------------------- |
| `last_min` | most recent index where `nums[i] == minK`            |
| `last_max` | most recent index where `nums[i] == maxK`            |
| `last_bad` | most recent index of a value outside `[minK, maxK]`  |

A subarray ending at `i` is valid when its start index:

- is **after** `last_bad` — so it contains no out-of-bounds value, **and**
- is **at or before** both `last_min` and `last_max` — so both bounds are
  present.

The number of such start indices is:

    min(last_min, last_max) - last_bad

clamped at `0` (in case `minK` or `maxK` has not appeared since the last
out-of-bounds value).

------------------------------------------------------------------------

## Implementation

``` python
def count_subarrays(nums, min_k, max_k):
    if min_k > max_k:
        return 0

    last_min = last_max = last_bad = -1
    total = 0

    for i, val in enumerate(nums):
        if val < min_k or val > max_k:
            last_bad = i
        if val == min_k:
            last_min = i
        if val == max_k:
            last_max = i

        total += max(0, min(last_min, last_max) - last_bad)

    return total
```

------------------------------------------------------------------------

## Complexity Analysis

- Time: O(n) — a single pass over the array
- Space: O(1) — only a few index trackers

------------------------------------------------------------------------

## Edge Cases

- `minK == maxK` → counts subarrays consisting solely of that value
- `minK` or `maxK` never appears → `0`
- A value outside `[minK, maxK]` splits the array into independent regions
- Degenerate bounds `minK > maxK` → `0`

------------------------------------------------------------------------

## Running the Tests

``` bash
python3 -m unittest solution -v
```

The test suite includes hand-picked cases plus a cross-check against a
brute-force O(n²) reference implementation over several inputs.

------------------------------------------------------------------------

## Summary

- Single pass, constant space
- Count subarrays by their ending index
- The trick is tracking the last occurrence of `minK`, `maxK`, and the last
  out-of-bounds value
