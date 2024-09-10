from typing import Optional

from algorithms.utils.sll import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next  # save the next node
            current.next = prev  # reverse the current node
            prev = current  # previous node is now the current node
            current = next_node  # move to the next node in the list

        return prev
