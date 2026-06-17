"""
Solution for the "Compare Version Numbers" problem.

This module provides:
- A two-pointer parser that compares version revisions without split()
- Unit tests using unittest
"""

# pylint: disable=invalid-name, missing-function-docstring, too-few-public-methods
import unittest


def compareVersion(version1: str, version2: str) -> int:
    """
    Compare two version strings revision by revision.

    Each revision is read as an integer, so leading zeros do not affect the
    comparison. Missing revisions are treated as 0 because the outer loop keeps
    running while either string still has characters left.

    Args:
        version1: First version string.
        version2: Second version string.

    Returns:
        -1 if version1 < version2, 1 if version1 > version2, otherwise 0.

    Example:
        compareVersion("1.01", "1.001") -> 0
    """
    i = j = 0
    n, m = len(version1), len(version2)

    while i < n or j < m:
        num1 = 0
        num2 = 0

        # Parse the next revision from version1.
        while i < n and version1[i] != ".":
            num1 = num1 * 10 + int(version1[i])
            i += 1

        # Parse the next revision from version2.
        while j < m and version2[j] != ".":
            num2 = num2 * 10 + int(version2[j])
            j += 1

        # The first different revision determines the result.
        if num1 > num2:
            return 1
        if num1 < num2:
            return -1

        # Skip the dot separator when present.
        if i < n and version1[i] == ".":
            i += 1
        if j < m and version2[j] == ".":
            j += 1

    return 0


# ---------------------------------------------------------------------------
# Unit Tests
# ---------------------------------------------------------------------------


class TestCompareVersion(unittest.TestCase):
    """Unit tests for compareVersion."""

    def test_equal_with_leading_zeros(self):
        self.assertEqual(compareVersion("1.01", "1.001"), 0)

    def test_equal_with_missing_revisions(self):
        self.assertEqual(compareVersion("1.0", "1.0.0"), 0)

    def test_version1_less_than_version2(self):
        self.assertEqual(compareVersion("0.1", "1.1"), -1)

    def test_version1_greater_than_version2(self):
        self.assertEqual(compareVersion("1.0.1", "1"), 1)

    def test_numeric_comparison_not_lexicographic(self):
        self.assertEqual(compareVersion("1.2", "1.10"), -1)

    def test_single_revision_greater(self):
        self.assertEqual(compareVersion("2", "1"), 1)

    def test_trailing_zero_revisions_do_not_change_value(self):
        self.assertEqual(compareVersion("7.5.2.4", "7.5.2.4.0"), 0)

    def test_later_revision_decides_result(self):
        self.assertEqual(compareVersion("1.0.0.1", "1.0.0.0"), 1)

    def test_large_revision_value(self):
        self.assertEqual(compareVersion("2147483647.0", "2147483646.9"), 1)


if __name__ == "__main__":
    unittest.main()
