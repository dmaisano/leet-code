import pytest

from algorithms.insert_greatest_common_divisors_in_linked_list import Solution
from algorithms.utils.sll import ListNode, sll_to_python_list


def test_determineGCD() -> None:
    soln = Solution()
    assert soln.determineGCD(48, 18) == 6
    assert soln.determineGCD(7, 5) == 1
    assert soln.determineGCD(100, 10) == 10
    assert soln.determineGCD(270, 192) == 6


def test_listInsert() -> None:
    soln = Solution()
    node = ListNode(1, ListNode(3))
    soln.listInsert(5, node)
    assert node.val == 1
    assert node.next.val == 5
    assert node.next.next.val == 3


def test_insertGreatestCommonDivisors() -> None:
    soln = Solution()
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


def test_insertGreatestCommonDivisors_single_element() -> None:
    soln = Solution()
    head = ListNode(5)
    new_head = soln.insertGreatestCommonDivisors(head)
    assert sll_to_python_list(new_head) == [5]


if __name__ == "__main__":
    pytest.main()
