from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val: int = val
        self.next: ListNode | None = next


def python_list_to_sll(values: List[int]) -> ListNode:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def sll_to_python_list(head: ListNode | None) -> List[int]:
    """Helper function to convert ListNode to Python list for easy comparison."""
    result: List[int] = []
    current: Optional[ListNode] = head
    while current is not None:
        result.append(current.val)
        current = current.next
    return result
