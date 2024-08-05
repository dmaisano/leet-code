from typing import Optional

import pytest

from .insert_greatest_common_divisors_in_linked_list import ListNode, Number, Solution


def sll_to_python_list(head: ListNode) -> list[Number]:
    """Helper function to convert ListNode to Python list for easy comparison."""
    result: list[Number] = []
    current: Optional[ListNode] = head
    while current is not None:
        result.append(current.val)
        current = current.next
    return result


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_determineGCD(solution: Solution) -> None:
    assert solution.determineGCD(48, 18) == 6
    assert solution.determineGCD(7, 5) == 1
    assert solution.determineGCD(100, 10) == 10
    assert solution.determineGCD(270, 192) == 6


def test_listInsert(solution: Solution) -> None:
    node = ListNode(1, ListNode(3))
    solution.listInsert(5, node)
    assert node.val == 1
    assert node.next.val == 5
    assert node.next.next.val == 3


def test_insertGreatestCommonDivisors(solution: Solution) -> None:
    head = ListNode(18, ListNode(48, ListNode(30)))
    new_head = solution.insertGreatestCommonDivisors(head)
    assert sll_to_python_list(new_head) == [18, 6, 48, 6, 30]

    head = ListNode(7, ListNode(5))
    new_head = solution.insertGreatestCommonDivisors(head)
    assert sll_to_python_list(new_head) == [7, 1, 5]

    head = ListNode(100, ListNode(10))
    new_head = solution.insertGreatestCommonDivisors(head)
    assert sll_to_python_list(new_head) == [100, 10, 10]

    head = None
    new_head = solution.insertGreatestCommonDivisors(head)
    assert new_head is None


def test_insertGreatestCommonDivisors_single_element(solution: Solution) -> None:
    head = ListNode(5)
    new_head = solution.insertGreatestCommonDivisors(head)
    assert sll_to_python_list(new_head) == [5]
