from typing import Optional
from numbers import Number


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: Number=0, next: Optional['ListNode']=None):
        self.val: Number = val
        self.next: ListNode | None = next


class Solution:
    def determineGCD(self, a: Number, b: Number):
        while b:
            a, b = b, a % b
        return a

    def listInsert(self, node: Optional[ListNode], val: Number) -> Optional[ListNode]:
        trail = node.next
        node.next = ListNode(val, trail)

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cursor = head

        skipCurrent = False
        while cursor.next is not None:
            nextValue = cursor.next.val or None

            if nextValue is None:
                break
            if skipCurrent is True:
                cursor = cursor.next
                skipCurrent = False
                continue

            gcd = self.determineGCD(cursor.val, nextValue)
            self.listInsert(cursor, gcd)
            cursor = cursor.next
            skipCurrent = True

        return head


if __name__ == "__main__":
    soln = Solution()
    sll = ListNode(18, ListNode(6, ListNode(10, ListNode(3))))

    res = soln.insertGreatestCommonDivisors(sll)
