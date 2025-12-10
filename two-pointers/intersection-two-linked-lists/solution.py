import unittest
from typing import Iterable, Optional


class ListNode:
    """A singly linked list node."""

    def __init__(self, val: int = 0, next_node: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next_node


# -----------------------------------------------------------
# Helpers for constructing test lists
# -----------------------------------------------------------
def build_list(values: Iterable[int]) -> Optional[ListNode]:
    """
    Construct a singly linked list from an iterable of integers.

    Args:
        values: Sequence of integer values to be turned into nodes.

    Returns:
        The head of the constructed linked list, or None if empty.
    """
    head: Optional[ListNode] = None
    cur: Optional[ListNode] = None

    for v in values:
        node = ListNode(v)
        if head is None:
            head = node
            cur = node
        else:
            cur.next = node  # type: ignore
            cur = node

    return head


def connect_lists_at_node(head_b: Optional[ListNode], node: Optional[ListNode]) -> None:
    """
    Connects the tail of list B to a given node, creating a true intersection.

    Args:
        head_b: Head of list B.
        node: The node at which list B should intersect list A.

    Notes:
        - If head_b is None, this function does nothing.
        - The `node` must be an existing node inside list A.
    """
    if head_b is None:
        return

    cur = head_b
    while cur.next:
        cur = cur.next
    cur.next = node


# -----------------------------------------------------------
# Solution under test
# -----------------------------------------------------------
def get_intersection_node(
    head_a: Optional[ListNode], head_b: Optional[ListNode]
) -> Optional[ListNode]:
    """
    Find the intersection node of two singly linked lists.

    Uses the pointer-switching technique:
    - Each pointer traverses A then B.
    - If lists intersect, the pointers meet at the intersection.
    - If not, both reach None at the same time.

    Args:
        head_a: Head of the first linked list.
        head_b: Head of the second linked list.

    Returns:
        The intersection ListNode, or None if no intersection exists.
    """
    ptr_a, ptr_b = head_a, head_b

    while ptr_a is not ptr_b:
        ptr_a = head_b if ptr_a is None else ptr_a.next
        ptr_b = head_a if ptr_b is None else ptr_b.next

    return ptr_a


# -----------------------------------------------------------
# Unit Tests
# -----------------------------------------------------------
class TestIntersectionNode(unittest.TestCase):
    """Unit tests for get_intersection_node function."""

    def test_intersection_middle(self) -> None:
        """
        A: 1 -> 2 -> [8 -> 9]
        B:       3 -> 4 ↗
        """
        common = build_list([8, 9])
        head_a = build_list([1, 2])
        head_b = build_list([3, 4])

        # Attach A tail → common
        cur = head_a
        while cur.next:
            cur = cur.next
        cur.next = common

        # Attach B tail → common
        cur = head_b
        while cur.next:
            cur = cur.next
        cur.next = common

        self.assertIs(get_intersection_node(head_a, head_b), common)

    def test_no_intersection(self) -> None:
        """Lists do not intersect."""
        head_a = build_list([1, 2, 3])
        head_b = build_list([4, 5])
        self.assertIsNone(get_intersection_node(head_a, head_b))

    def test_intersection_at_head(self) -> None:
        """A and B share the exact same head node."""
        common = build_list([1, 2, 3])
        head_a = head_b = common
        self.assertIs(get_intersection_node(head_a, head_b), common)

    def test_one_empty_list(self) -> None:
        """One list is empty, the other is not."""
        head_a = None
        head_b = build_list([1, 2, 3])
        self.assertIsNone(get_intersection_node(head_a, head_b))

    def test_both_empty(self) -> None:
        """Both lists are empty."""
        self.assertIsNone(get_intersection_node(None, None))

    def test_different_lengths_no_intersection(self) -> None:
        """
        A: 1 → 2 → 3 → 4 → 5
        B: 9 → 8
        No intersection. Algorithm should terminate normally.
        """
        head_a = build_list([1, 2, 3, 4, 5])
        head_b = build_list([9, 8])
        self.assertIsNone(get_intersection_node(head_a, head_b))


if __name__ == "__main__":
    unittest.main()
