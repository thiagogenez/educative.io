from typing import List


def max_subsequence(nums: List[int], k: int) -> List[int]:
    """
    Return the lexicographically largest subsequence of length `k` from `nums`,
    preserving the original order of digits.

    This implementation uses a greedy "upgrade" strategy rather than the
    classical monotonic-stack approach.

    Algorithm overview:
        1. Initialize the subsequence using the first `k` digits of `nums`.
        2. For each subsequent digit `x` in nums[k:]:
            - Consider all possible subsequences obtained by removing one
                element from the current subsequence and appending `x`.
            - Among those `k` candidates, keep only the lexicographically
                largest sequence.
        3. After processing all remaining digits, the accumulated subsequence
        represents the maximum achievable lexicographical value of length `k`.


    Time complexity:
        O((n - k) * k), since each of the (n - k) remaining digits generates
        up to `k` candidate sequences for comparison.

    Args:
        nums : List[int]
            The source sequence of digits.
        k : int
            Desired length of the output subsequence.

    Returns:
        List[int] : The lexicographically largest subsequence of length `k`.
    """
    # Edge cases
    if k <= 0:
        return []
    if k >= len(nums):
        return nums[:]

    # Start with the first k digits
    sub = nums[:k]

    # Iterate over all remaining digits
    for digit in nums[k:]:

        # Best candidate for this round starts as the current subsequence
        best = sub[:]

        # Try replacing each of the k positions with this new digit at the end
        for j in range(k):
            cand = sub[:j] + sub[j + 1 :] + [digit]

            # Use Python's lexicographical list comparison
            if cand > best:
                best = cand[:]  # capture best candidate

        # Update subsequence after testing all possibilities
        sub = best

    # Return the best subsequence found
    return sub


def merge(a: List[int], b: List[int]) -> List[int]:
    """
    Merge two digit sequences a and b into the lexicographically largest possible result.
    We do this by always choosing the next digit from the sequence whose *remaining suffix*
    is lexicographically larger.

    Example:
        a = [6,7]
        b = [6,0,4]
        Comparing suffixes:
            [6,7] > [6,0,4]  -> pick from a
    """
    # pointers for a and b
    i = j = 0

    # result sequence
    result = []

    # While both lists still have digits available
    while i < len(a) and j < len(b):

        # Compare lexicographically the remaining suffixes
        if a[i:] > b[j:]:
            result.append(a[i])  # choose digit from a
            i += 1
        else:
            result.append(b[j])  # choose digit from b
            j += 1

    # One of the lists ended. Append whatever remains.
    result.extend(a[i:])
    result.extend(b[j:])

    return result


def max_number(nums1: List[int], nums2: List[int], k: int) -> List[int]:
    """
    Combine digits from nums1 and nums2 to form the largest possible number
    of length k while preserving the relative order of digits in each array.

    Strategy:
      - Try all valid splits where we take `i` digits from nums1
        and `k - i` digits from nums2.
      - For each split:
           1. Extract the best subsequence of size i from nums1.
           2. Extract the best subsequence of size k-i from nums2.
           3. Merge the two subsequences into the lexicographically largest result.
           4. Track the best merged sequence overall.
    """
    n, m = len(nums1), len(nums2)

    # Track the best merged result and its numeric value
    best = []

    # Try all possible ways to choose i digits from nums1
    # i ranges from:
    #   max(0, k - m)  => minimum digits needed from nums1
    #   to
    #   min(k, n)      => cannot take more than nums1 length
    for i in range(max(0, k - m), min(k, n) + 1):

        # Best subsequence of length i from nums1
        left = max_subsequence(nums1, i)

        # Best subsequence of length k - i from nums2
        right = max_subsequence(nums2, k - i)

        # Merge to get the best possible number for this split
        merged = merge(left, right)

        # Update global best if this merged result is larger
        if merged > best:
            best = merged

    return best


# ------------------------------------------------------------
# MAIN
# ------------------------------------------------------------
def main():
    print("Running sample test cases...\n")

    tests = [
        ([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5, [9, 8, 6, 5, 3]),
        ([6, 7], [6, 0, 4], 5, [6, 7, 6, 0, 4]),
        ([3, 9], [8, 9], 3, [9, 8, 9]),
        ([1, 2, 3], [4, 5, 6], 4, [6, 1, 2, 3]),
        ([9, 1, 2], [3, 4, 9], 3, [9, 9, 2]),
        ([5, 5, 1], [9, 1, 1], 3, [9, 5, 5]),
    ]

    for nums1, nums2, k, expected in tests:
        result = max_number(nums1, nums2, k)

        print(f"nums1 = {nums1}")
        print(f"nums2 = {nums2}")
        print(f"k = {k}")
        print(f"result = {result}")

        # If expected is provided => use assertion
        try:
            assert result == expected, (
                f"Test failed!\n" f"Expected: {expected}\n" f"Got:      {result}\n"
            )
            print("Test passed!")
        except AssertionError as e:
            print(e)

        print("-" * 50)


if __name__ == "__main__":
    main()
