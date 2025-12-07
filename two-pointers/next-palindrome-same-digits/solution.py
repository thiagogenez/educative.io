"""Next Palindrome with Same Digits Problem Solution."""

from typing import List
import unittest


def next_permutation(digits: List[int]) -> bool:
    """
    Transform the list of digits into the next lexicographical permutation
    in-place.

    Returns:
        True if a next permutation exists (and `digits` was modified),
        False if it's already the highest permutation.
    """
    # Find the rightmost index 'i' where digits[i] < digits[i + 1]
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    # No such index → digits are in non-increasing order, no next permutation
    if i < 0:
        return False

    # Find the rightmost element greater than digits[i]
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1

    # Swap them
    digits[i], digits[j] = digits[j], digits[i]

    # Reverse the suffix to get the smallest suffix after position i
    digits[i + 1 :] = digits[i + 1 :][::-1]

    return True


def find_next_palindrome(num_str: str) -> str:
    """
    Given a numeric string, compute the next palindrome that can be formed by
    taking the left half, finding its next permutation, and mirroring it.

    Returns:
        The next palindrome as a string, or an empty string if none exists.
    """
    n = len(num_str)
    if n <= 1:
        return ""

    # Convert string to list of digits
    digits = [int(ch) for ch in num_str]

    # Split into left half and middle (if odd length)
    middle, left = [digits[n // 2]] if n % 2 else [], digits[: n // 2]

    if not next_permutation(left):
        return ""

    # Build palindrome: left + middle + reversed(left)
    return "".join(str(d) for d in left + middle + left[::-1])


# ==========================
#        UNIT TESTS
# ==========================
class TestNextPermutation(unittest.TestCase):
    """Unit tests for the next_permutation function."""

    def test_simple_increase(self):
        """Simple case: 123 -> 132"""
        digits = [1, 2, 3]
        result = next_permutation(digits)
        self.assertTrue(result)
        self.assertEqual(digits, [1, 3, 2])

    def test_multiple_steps(self):
        """Multiple steps: 132 -> 213"""
        digits = [1, 3, 2]
        result = next_permutation(digits)
        self.assertTrue(result)
        self.assertEqual(digits, [2, 1, 3])

    def test_already_max(self):
        """Already the largest permutation: 321 -> no next"""
        digits = [3, 2, 1]
        result = next_permutation(digits)
        self.assertFalse(result)
        self.assertEqual(digits, [3, 2, 1])

    def test_all_equal(self):
        """All digits equal: 111 -> no next"""
        digits = [1, 1, 1]
        result = next_permutation(digits)
        self.assertFalse(result)
        self.assertEqual(digits, [1, 1, 1])

    def test_in_place_behavior(self):
        """Check that the input list is modified in-place."""
        digits = [1, 2, 3]
        ref = digits
        next_permutation(digits)
        self.assertIs(digits, ref)  # same object, modified in-place


class TestFindNextPalindrome(unittest.TestCase):
    """Unit tests for the find_next_palindrome function."""

    def test_example_from_statement(self):
        """Example given in the problem statement."""
        self.assertEqual(find_next_palindrome("123321"), "132231")

    def test_even_length(self):
        """Even length case: 1221 -> 2112"""
        self.assertEqual(find_next_palindrome("1221"), "2112")

    def test_odd_length(self):
        """Odd length case: 12321 -> 21312"""
        self.assertEqual(find_next_palindrome("12321"), "21312")

    def test_all_digits_equal(self):
        """All digits equal: 111111 -> no next"""
        self.assertEqual(find_next_palindrome("111111"), "")
        self.assertEqual(find_next_palindrome("999999"), "")

    def test_single_digit(self):
        """Single digit case: no next palindrome"""
        self.assertEqual(find_next_palindrome("1"), "")
        self.assertEqual(find_next_palindrome("9"), "")

    def test_already_largest(self):
        """Input already yields the lexicographically largest
        palindrome from these digits -> no next palindrome"""
        self.assertEqual(find_next_palindrome("543345"), "")

    def test_typical_even_case(self):
        """Typical even-length case: 889988 -> 898898"""
        self.assertEqual(find_next_palindrome("889988"), "898898")

    def test_other_valid_case(self):
        """Another valid case: 455554 -> 545545"""
        self.assertEqual(find_next_palindrome("455554"), "545545")

    def test_result_is_palindrome(self):
        """Ensure the result (when non-empty) is actually a palindrome"""
        s = "123321"
        result = find_next_palindrome(s)
        self.assertNotEqual(result, "")  # sanity: should exist
        self.assertEqual(result, result[::-1])  # must be palindrome

    def test_result_is_strictly_greater(self):
        """ "Ensure the result (when non-empty) is strictly greater than input"""
        s = "123321"
        result = find_next_palindrome(s)
        self.assertGreater(result, s)

    def test_same_digits_multiset(self):
        """Ensure the result (if any) uses exactly the same multiset of digits"""
        for s in ["123321", "1221", "12321", "889988", "455554"]:
            result = find_next_palindrome(s)
            if result:
                self.assertEqual(sorted(s), sorted(result))


if __name__ == "__main__":
    unittest.main()
