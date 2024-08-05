from typing import Optional, TypeAlias, Union

Number: TypeAlias = Union[int, float]


class ListNode:
    def __init__(self, val: Number = 0, next: Optional["ListNode"] = None):
        self.val: int | float = val
        self.next: ListNode | None = next


class Solution:
    def determineGCD(self, a: Number, b: Number) -> Number:
        while b:
            a, b = b, a % b
        return a

    def listInsert(self, val: Number, node: Optional[ListNode] = None) -> None:
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
