"""
Solution for the "Count Subarrays With Fixed Bounds" problem.

This module provides:
- A single-pass O(n) algorithm to count fixed-bound subarrays
- Unit tests using unittest

A fixed-bound subarray is a contiguous slice whose minimum equals `minK`
and whose maximum equals `maxK`.
"""

# pylint: disable=missing-function-docstring, too-few-public-methods, too-many-public-methods
from typing import List
import unittest


def count_subarrays(nums: List[int], min_k: int, max_k: int) -> int:
    """
    Count the number of fixed-bound subarrays in `nums`.

    A subarray is fixed-bound when its smallest value equals `min_k` and
    its largest value equals `max_k`.

    Single-pass idea: for each index `i`, count the valid subarrays that
    END at `i`. Track three positions:
      - last_min: most recent index where nums[i] == min_k
      - last_max: most recent index where nums[i] == max_k
      - last_bad: most recent index of a value outside [min_k, max_k]

    A subarray ending at `i` is valid iff its start is after `last_bad`
    (no out-of-bounds element) and at or before both `last_min` and
    `last_max` (so both bounds are present). The number of such starts is
    `min(last_min, last_max) - last_bad`, clamped at 0.

    Args:
        nums: List of integers.
        min_k: Required minimum value of a fixed-bound subarray.
        max_k: Required maximum value of a fixed-bound subarray.

    Returns:
        int: The count of fixed-bound subarrays.

    Example:
        nums = [1, 3, 5, 2, 7, 5], min_k = 1, max_k = 5 -> 2
    """
    # If min_k > max_k, no subarray can satisfy both bounds.
    if min_k > max_k:
        return 0

    last_min = -1
    last_max = -1
    last_bad = -1
    total = 0

    for i, val in enumerate(nums):
        # Value outside the bounds breaks every subarray that would span it.
        if val < min_k or val > max_k:
            last_bad = i
        # Update the last seen positions of min_k and max_k.
        if val == min_k:
            last_min = i
        if val == max_k:
            last_max = i

        # For a subarray ending at i, the start can be anywhere from
        # (last_bad + 1) up to min(last_min, last_max):
        #   - (last_bad + 1) keeps all out-of-bounds values out
        #   - min(last_min, last_max) guarantees both min_k and max_k are in
        # Number of those starts = min(last_min, last_max) - last_bad.
        total += max(0, min(last_min, last_max) - last_bad)

    return total


# ---------------------------------------------------------------------------
# Unit Tests
# ---------------------------------------------------------------------------


class TestCountSubarrays(unittest.TestCase):
    """Unit tests for count_subarrays."""

    @staticmethod
    def brute_force(nums: List[int], min_k: int, max_k: int) -> int:
        """Reference O(n^2) implementation used to cross-check results."""
        count = 0
        n = len(nums)
        for start in range(n):
            cur_min = cur_max = nums[start]
            for end in range(start, n):
                cur_min = min(cur_min, nums[end])
                cur_max = max(cur_max, nums[end])
                if cur_min == min_k and cur_max == max_k:
                    count += 1
        return count

    def test_example_1(self):
        # Subarrays: [1,3,5] and [1,3,5,2] -> 2
        self.assertEqual(count_subarrays([1, 3, 5, 2, 7, 5], 1, 5), 2)

    def test_example_2(self):
        # min_k == max_k: count subarrays made only of that value.
        # [1,1,1,1] with k=1 -> 4 + 3 + 2 + 1 = 10
        self.assertEqual(count_subarrays([1, 1, 1, 1], 1, 1), 10)

    def test_no_valid_subarray(self):
        # max_k never appears.
        self.assertEqual(count_subarrays([1, 1, 1], 1, 2), 0)

    def test_min_only_present(self):
        # Only min_k appears, max_k missing -> 0.
        self.assertEqual(count_subarrays([2, 2, 2], 1, 2), 0)

    def test_out_of_bounds_splits(self):
        # A value above max_k splits the array into independent regions.
        self.assertEqual(count_subarrays([1, 5, 9, 1, 5], 1, 5), 2)

    def test_single_pair(self):
        self.assertEqual(count_subarrays([1, 2], 1, 2), 1)

    def test_min_greater_than_max(self):
        # Degenerate bounds: impossible to satisfy.
        self.assertEqual(count_subarrays([1, 2, 3], 3, 1), 0)

    def test_all_out_of_bounds(self):
        self.assertEqual(count_subarrays([10, 20, 30], 1, 5), 0)

    def test_matches_brute_force(self):
        # Cross-check against the reference implementation on varied inputs.
        cases = [
            ([1, 3, 5, 2, 7, 5], 1, 5),
            ([1, 1, 1, 1], 1, 1),
            ([5, 1, 4, 2, 3, 5, 1], 1, 5),
            ([2, 1, 3, 1, 2, 4, 1, 3], 1, 3),
            ([4, 4, 4, 4, 4], 4, 4),
            ([1, 2, 3, 4, 5, 6], 2, 5),
        ]
        for nums, min_k, max_k in cases:
            with self.subTest(nums=nums, min_k=min_k, max_k=max_k):
                self.assertEqual(
                    count_subarrays(nums, min_k, max_k),
                    self.brute_force(nums, min_k, max_k),
                )


if __name__ == "__main__":
    unittest.main()
