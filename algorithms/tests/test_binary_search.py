from typing import List

import pytest

from algorithms.binary_search import Solution


@pytest.mark.parametrize(
    "nums, target, expected_output",
    [
        ([1, 2, 3, 4, 5], 3, 2),  # Target in the middle
        ([1, 2, 3, 4, 5], 1, 0),  # Target at the beginning
        ([1, 2, 3, 4, 5], 5, 4),  # Target at the end
        ([1, 2, 3, 4, 5], 6, -1),  # Target not in list
        ([], 1, -1),  # Empty list
        ([1], 1, 0),  # Single element list, target present
        ([1], 0, -1),  # Single element list, target absent
        ([1, 2, 3, 4, 5], -1, -1),  # Target less than all elements
        ([1, 2, 3, 4, 5], 10, -1),  # Target greater than all elements
        (
            [1, 1, 1, 1, 1],
            1,
            2,
        ),  # All elements the same, target present (will return the middle)
        ([1, 1, 1, 1, 1], 2, -1),  # All elements the same, target absent
    ],
)
def test_search(nums: List[int], target: int, expected_output: int) -> None:
    solution = Solution()
    result = solution.search(nums, target)
    assert result == expected_output, f"Failed for nums={nums}, target={target}"


if __name__ == "__main__":
    pytest.main()
