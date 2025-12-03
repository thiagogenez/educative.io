import unittest

MOD = 10**9 + 7


def maxsum(nums1, nums2):
    """
    Returns the maximum score achievable by traversing two sorted arrays.
    Uses a two-pointer technique to traverse both arrays, accumulating sums
    until a common element is found, at which point the maximum of the two
    accumulated sums is added to the total score. The process continues until
    both arrays are fully traversed.

    Args:
        nums1 (List[int]): First sorted array.
        nums2 (List[int]): Second sorted array.

        Returns:
            int: The maximum score achievable by traversing the two arrays
    """
    i = j = 0
    n, m = len(nums1), len(nums2)
    sum1 = sum2 = total = 0

    while i < n or j < m:

        # ---------------------------
        # 1) nums2 is exhausted => take from nums1
        # ---------------------------
        if j == m:
            sum1 += nums1[i]
            i += 1

        # ---------------------------
        # 2) nums1 is exhausted => take from nums2
        # ---------------------------
        elif i == n:
            sum2 += nums2[j]
            j += 1

        # ---------------------------
        # 3) nums1 < nums2 => advance nums1
        # ---------------------------
        elif nums1[i] < nums2[j]:
            sum1 += nums1[i]
            i += 1

        # ---------------------------
        # 4) nums2 < nums1 => advance nums2
        # ---------------------------
        elif nums2[j] < nums1[i]:
            sum2 += nums2[j]
            j += 1

        # ---------------------------
        # 5) equal values => shared point!
        # ---------------------------
        else:
            val = nums1[i]  # same as nums2[j]
            sum1 += val
            sum2 += val

            total += max(sum1, sum2)

            # reset partial sums
            sum1 = sum2 = 0

            i += 1
            j += 1

    # Add remaining tail
    total += max(sum1, sum2)
    return total % MOD


class TestMaxSum(unittest.TestCase):
    """Unit tests for the maxsum function."""

    def test_basic(self):
        """Basic test case from the prompt."""
        self.assertEqual(maxsum([1, 3, 5, 7, 9], [1, 2, 3, 4, 5]), 31)

    def test_no_shared(self):
        """With no shared elements, you just pick the array with the largest sum"""
        a = [1, 2, 3]
        b = [4, 5, 6]
        expected = max(sum(a), sum(b)) % MOD
        self.assertEqual(maxsum(a, b), expected)

    def test_all_shared(self):
        """All elements shared -> you effectively traverse a single set of uniques"""
        a = [1, 2, 3]
        b = [1, 2, 3]
        expected = sum(a) % MOD
        self.assertEqual(maxsum(a, b), expected)

    def test_shared_in_middle(self):
        """Shared elements in the middle of the arrays"""
        a = [2, 4, 6, 8]
        b = [1, 6, 7, 9]
        expected = (max(2 + 4 + 6, 1 + 6) + max(8, 7 + 9)) % MOD  # 28
        self.assertEqual(maxsum(a, b), expected)

    def test_single_element(self):
        """Single shared element => counted once"""
        self.assertEqual(maxsum([5], [5]), 5)

    def test_large_values(self):
        """Large value, ensure modulo is applied correctly"""
        x = 10**9
        expected = x % MOD
        self.assertEqual(maxsum([x], [x]), expected)

    def test_one_empty(self):
        """If one array is empty, you must take the other completely"""
        self.assertEqual(maxsum([], [1, 2, 3]), sum([1, 2, 3]) % MOD)
        self.assertEqual(maxsum([1, 2, 3], []), sum([1, 2, 3]) % MOD)


if __name__ == "__main__":
    unittest.main()
