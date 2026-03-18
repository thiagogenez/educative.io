"""
Solution for the "Remove Element" problem.

This module provides:
- An in-place algorithm to remove all occurrences of a value from a list
- Unit tests using unittest

The algorithm does NOT preserve order (which is allowed by the problem).
"""

# pylint: disable=missing-function-docstring, too-few-public-methods, too-many-public-methods
from typing import List
import unittest


def remove_element(nums: List[int], val: int) -> int:
    """
    Remove all occurrences of `val` from `nums` in-place.

    This uses a two-pointer approach:
    - `i` scans from the beginning
    - `k` tracks the end of the "valid" region

    When a match is found at `i`, it is swapped with a non-matching
    element from the end.

    Args:
        nums: List of integers to modify in-place.
        val: Value to remove.

    Returns:
        int: Number of elements not equal to `val` (k).
             The first k elements of nums contain the result.

    Example:
        nums = [3,2,2,3], val = 3
        -> returns 2, nums becomes [2,2,_,_]
    """
    i = 0
    k = len(nums) - 1

    # Process elements until pointers cross
    while i <= k:
        # Skip invalid values at the end
        if nums[k] == val:
            k -= 1
            continue

        # Swap current invalid value with a valid one from the end
        if nums[i] == val:
            nums[i], nums[k] = nums[k], nums[i]
            k -= 1

        # Move forward pointer
        i += 1

    # Number of valid elements
    return k + 1


# ---------------------------------------------------------------------------
# Unit Tests
# ---------------------------------------------------------------------------


class TestRemoveElement(unittest.TestCase):
    """
    Unit tests for remove_element.

    Since order does NOT matter, we:
    - Check the length (k)
    - Check the elements using assertCountEqual
    """

    def assert_valid_result(self, original, val, nums, k):
        """
        Helper to validate correctness of result.
        """
        expected = [x for x in original if x != val]

        # Validate count
        self.assertEqual(k, len(expected))

        # Validate elements (order-independent)
        self.assertCountEqual(nums[:k], expected)

        # Ensure removed value is not present
        for x in nums[:k]:
            self.assertNotEqual(x, val)

    def test_example_1(self):
        nums = [3, 2, 2, 3]
        original = nums[:]
        k = remove_element(nums, 3)
        self.assert_valid_result(original, 3, nums, k)

    def test_example_2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        original = nums[:]
        k = remove_element(nums, 2)
        self.assert_valid_result(original, 2, nums, k)

    def test_empty_array(self):
        nums = []
        original = nums[:]
        k = remove_element(nums, 1)
        self.assert_valid_result(original, 1, nums, k)

    def test_all_elements_match(self):
        nums = [1, 1, 1, 1]
        original = nums[:]
        k = remove_element(nums, 1)
        self.assert_valid_result(original, 1, nums, k)

    def test_no_elements_match(self):
        nums = [4, 5, 6]
        original = nums[:]
        k = remove_element(nums, 3)
        self.assert_valid_result(original, 3, nums, k)

    def test_single_element_match(self):
        nums = [7]
        original = nums[:]
        k = remove_element(nums, 7)
        self.assert_valid_result(original, 7, nums, k)

    def test_single_element_no_match(self):
        nums = [7]
        original = nums[:]
        k = remove_element(nums, 3)
        self.assert_valid_result(original, 3, nums, k)

    def test_mixed_values(self):
        nums = [2, 3, 2, 4, 5, 2, 6]
        original = nums[:]
        k = remove_element(nums, 2)
        self.assert_valid_result(original, 2, nums, k)


if __name__ == "__main__":
    unittest.main()
