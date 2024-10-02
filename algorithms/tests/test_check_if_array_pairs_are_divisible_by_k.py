from typing import List

import pytest

from algorithms.check_if_array_pairs_are_divisible_by_k import Solution


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([1, 2, 3, 4, 5, 10, 6, 7, 8, 9], 5, True),
        ([1, 2, 3, 4, 5, 6], 7, True),
        ([1, 2, 3, 4, 5, 6], 10, False),
        ([-10, 10], 2, True),
        ([-1, 1, -2, 2, -3, 3, -4, 4], 3, True),
        ([1, 2, 3, 4, 5, 6], 1, True),
        ([1, 2, 3, 4, 5, 6], 2, False),
        ([1, 2, 3, 4, 5, 6], 3, True),
        ([i for i in range(1, 1001)], 7, True),
    ],
)
def test_canArrange(arr: List[int], k: int, expected: bool) -> None:
    solution = Solution()
    assert solution.canArrange(arr, k) == expected


if __name__ == "__main__":
    pytest.main()
