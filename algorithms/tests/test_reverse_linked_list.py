from typing import List, Optional

import pytest

from ..reverse_linked_list import ListNode, Solution


def create_linked_list(values: List[Optional[int]]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[Optional[int]]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


@pytest.mark.parametrize(
    "input_list, expected_reversed_list",
    [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1], [1]),
        ([], []),
        ([10, 20, 30], [30, 20, 10]),
    ],
)
def test_reverseList(input_list: List[int], expected_reversed_list: List[int]) -> None:
    # Arrange
    solution = Solution()
    head = create_linked_list(input_list)

    # Act
    reversed_head = solution.reverseList(head)
    result_list = linked_list_to_list(reversed_head)

    # Assert
    assert result_list == expected_reversed_list


if __name__ == "__main__":
    pytest.main()
