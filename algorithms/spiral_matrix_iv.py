from typing import List, Optional

from algorithms.utils.sll import ListNode


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        # Initialize matrix with -1
        matrix = [[-1] * n for _ in range(m)]

        # Define boundaries
        top, bottom, left, right = 0, m - 1, 0, n - 1
        curr = head

        while curr and top <= bottom and left <= right:
            # Fill the top row, moving left to right
            for i in range(left, right + 1):
                if curr:
                    matrix[top][i] = curr.val
                    curr = curr.next
                else:
                    break
            top += 1
            if top > bottom:
                break

            # Fill the right column, moving top to bottom
            for i in range(top, bottom + 1):
                if curr:
                    matrix[i][right] = curr.val
                    curr = curr.next
                else:
                    break
            right -= 1
            if right < left:
                break

            # Fill the bottom row, moving right to left
            for i in range(right, left - 1, -1):
                if curr:
                    matrix[bottom][i] = curr.val
                    curr = curr.next
                else:
                    break
            bottom -= 1
            if bottom < top:
                break

            # Fill the left column, moving bottom to top
            for i in range(bottom, top - 1, -1):
                if curr:
                    matrix[i][left] = curr.val
                    curr = curr.next
                else:
                    break
            left += 1

        return matrix
