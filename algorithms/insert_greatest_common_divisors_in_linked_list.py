from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val: int = val
        self.next: ListNode | None = next


class Solution:
    def determineGCD(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def listInsert(self, val: int, node: Optional[ListNode] = None) -> None:
        if node is not None:
            trail = node.next
            node.next = ListNode(val, trail)

    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode] = None
    ) -> ListNode | None:
        if not head or head.next is None:
            return head

        cursor = head
        while cursor.next is not None:
            nextValue = cursor.next.val or None

            if nextValue is None:
                break

            gcd = self.determineGCD(cursor.val, nextValue)
            self.listInsert(gcd, cursor)
            cursor = cursor.next
            if cursor.next:
                cursor = cursor.next

        return head
