# Compare Version Numbers

## Problem Statement

Given two version strings, `version1` and `version2`, compare them.

A version string is composed of revisions separated by dots (`.`). Each
revision's value is determined by converting it to an integer, ignoring any
leading zeros.

Compare the two version strings by evaluating their revision values from left
to right. If one version string contains fewer revisions than the other, treat
each missing revision as `0`.

Return the result of the comparison as follows:

- Return `-1` if `version1` is less than `version2`
- Return `1` if `version1` is greater than `version2`
- Return `0` if both versions are equal

Note: Each revision value in `version1` and `version2` is guaranteed to fit
within a 32-bit integer.

------------------------------------------------------------------------

## Constraints

- `1 <= version1.length, version2.length <= 500`
- `version1` and `version2` contain only digits and `.`
- `version1` and `version2` are valid version numbers
- All given revisions in `version1` and `version2` can be stored in a
  32-bit integer

------------------------------------------------------------------------

## Example

```python
version1 = "1.01"
version2 = "1.001"
```

Output:

```text
0
```

Explanation:

Both versions have the same revision values: `[1, 1]`.

------------------------------------------------------------------------

## Approach

This solution uses a two-pointer technique:

- `i` scans `version1`
- `j` scans `version2`
- For each revision, build the integer value digit by digit
- Compare the current revision values immediately
- If one version has no revision at the current position, use `0`

This avoids creating arrays with `split()` and compares each character only
once.

------------------------------------------------------------------------

## Implementation

```python
def compareVersion(version1, version2):
    i = j = 0
    n, m = len(version1), len(version2)

    while i < n or j < m:
        num1 = 0
        num2 = 0

        while i < n and version1[i] != ".":
            num1 = num1 * 10 + int(version1[i])
            i += 1

        while j < m and version2[j] != ".":
            num2 = num2 * 10 + int(version2[j])
            j += 1

        if num1 > num2:
            return 1

        if num1 < num2:
            return -1

        if i < n and version1[i] == ".":
            i += 1
        if j < m and version2[j] == ".":
            j += 1

    return 0
```

------------------------------------------------------------------------

## Complexity Analysis

- Time: O(n + m), where `n` and `m` are the lengths of the two version strings
- Space: O(1), because only counters and revision values are stored

------------------------------------------------------------------------

## Edge Cases

- Leading zeros: `"1.01"` and `"1.001"` are equal
- Missing revisions: `"1.0"` and `"1.0.0"` are equal
- Different revision values: `"1.2"` is less than `"1.10"`
- Single revision versions: `"2"` is greater than `"1"`

------------------------------------------------------------------------

## Summary

- Compare revisions from left to right
- Convert each revision to an integer to ignore leading zeros
- Treat missing revisions as `0`
- Stop as soon as one revision differs
