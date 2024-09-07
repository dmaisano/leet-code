from typing import List, Optional

import pytest

from ..insert_greatest_common_divisors_in_linked_list import ListNode, Solution


def sll_to_python_list(head: ListNode) -> List[int]:
    """Helper function to convert ListNode to Python list for easy comparison."""
    result: List[int] = []
    current: Optional[ListNode] = head
    while current is not None:
        result.append(current.val)
        current = current.next
    return result


@pytest.fixture
def soln() -> Solution:
    return Solution()


def test_determineGCD(soln: Solution) -> None:
    assert soln.determineGCD(48, 18) == 6
    assert soln.determineGCD(7, 5) == 1
    assert soln.determineGCD(100, 10) == 10
    assert soln.determineGCD(270, 192) == 6


def test_listInsert(soln: Solution) -> None:
    node = ListNode(1, ListNode(3))
    soln.listInsert(5, node)
    assert node.val == 1
    assert node.next.val == 5
    assert node.next.next.val == 3


def test_insertGreatestCommonDivisors(soln: Solution) -> None:
    head = ListNode(18, ListNode(48, ListNode(30)))
    new_head = soln.insertGreatestCommonDivisors(head)
    assert sll_to_python_list(new_head) == [18, 6, 48, 6, 30]

    head = ListNode(7, ListNode(5))
    new_head = soln.insertGreatestCommonDivisors(head)
    assert sll_to_python_list(new_head) == [7, 1, 5]

    head = ListNode(100, ListNode(10))
    new_head = soln.insertGreatestCommonDivisors(head)
    assert sll_to_python_list(new_head) == [100, 10, 10]

    head = None
    new_head = soln.insertGreatestCommonDivisors(head)
    assert new_head is None


def test_insertGreatestCommonDivisors_single_element(soln: Solution) -> None:
    head = ListNode(5)
    new_head = soln.insertGreatestCommonDivisors(head)
    assert sll_to_python_list(new_head) == [5]


if __name__ == "__main__":
    pytest.main()
