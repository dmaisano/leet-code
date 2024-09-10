from typing import List

import pytest

from algorithms.spiral_matrix_iv import Solution
from algorithms.utils.sll import ListNode, python_list_to_sll


@pytest.mark.parametrize(
    "m, n, linked_list_values, expected",
    [
        # Test case 1: Perfectly fills the matrix
        (3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9], [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
        # Test case 2: Matrix with more cells than linked list elements, expect -1 in remaining spots
        (3, 3, [1, 2, 3, 4, 5], [[1, 2, 3], [-1, -1, 4], [-1, -1, 5]]),
        # Test case 3: Linked list has more elements than the matrix can hold
        (2, 2, [1, 2, 3, 4, 5, 6], [[1, 2], [4, 3]]),
        # Test case 4: 1x1 matrix with one element in the linked list
        (1, 1, [42], [[42]]),
        # Test case 5: Empty linked list, expect matrix filled with -1
        (2, 2, [], [[-1, -1], [-1, -1]]),
        # Test case 6: 3x2 matrix with fewer elements than required
        (3, 2, [1, 2, 3], [[1, 2], [-1, 3], [-1, -1]]),
    ],
)
def test_spiralMatrix(
    m: int, n: int, linked_list_values: List[int], expected: List[List[int]]
) -> None:
    head: ListNode = python_list_to_sll(linked_list_values)
    result = Solution().spiralMatrix(m, n, head)
    assert result == expected


if __name__ == "__main__":
    pytest.main()
