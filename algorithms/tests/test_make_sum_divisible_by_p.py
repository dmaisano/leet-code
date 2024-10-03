from typing import List
import pytest

from algorithms.make_sum_divisible_by_p import Solution


@pytest.mark.parametrize(
    "nums, p, expected",
    [
        ([3, 1, 4, 2], 6, 1),  # Removing [4] makes the sum 6, which is divisible by 6
        (
            [6, 3, 5, 2],
            9,
            2,
        ),  # Removing [6, 3] makes the sum 7, which is divisible by 9
        ([1, 2, 3], 3, 0),  # The sum is already divisible by 3
        ([1, 2, 3], 7, -1),  # No subarray can make the sum divisible by 7
        (
            [1, 2, 3, 4, 5, 6],
            5,
            1,
        ),  # Removing [6] makes the sum 15, which is divisible by 5
        ([1, 2, 3, 4], 10, 0),  # The sum is already divisible by 10
    ],
)
def test_minSubarray(nums: List[int], p: int, expected: int) -> None:
    solution = Solution()
    assert solution.minSubarray(nums, p) == expected
