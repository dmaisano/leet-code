from typing import List

import pytest

from algorithms.longest_subarray_with_maximum_bitwise_and import Solution


def test_example_case_1() -> None:
    soln = Solution()
    nums = [1, 2, 3, 3, 2, 2]
    assert soln.longestSubarray(nums) == 2


def test_example_case_2() -> None:
    soln = Solution()
    nums = [1, 2, 3, 4]
    assert soln.longestSubarray(nums) == 1


def test_single_element_array() -> None:
    soln = Solution()
    nums = [7]
    assert soln.longestSubarray(nums) == 1


def test_all_same_elements() -> None:
    soln = Solution()
    nums = [5, 5, 5, 5]
    assert soln.longestSubarray(nums) == 4


def test_two_max_elements() -> None:
    soln = Solution()
    nums = [2, 3, 3, 2, 1]
    assert soln.longestSubarray(nums) == 2


def test_max_value_at_end() -> None:
    soln = Solution()
    nums = [1, 2, 1, 5, 5]
    assert soln.longestSubarray(nums) == 2


def test_large_input_with_multiple_max() -> None:
    soln = Solution()
    nums = [4] * 10000  # All elements are the maximum (4)
    assert soln.longestSubarray(nums) == 10000


def test_no_repeated_max() -> None:
    soln = Solution()
    nums = [10, 9, 8, 7, 6]
    assert soln.longestSubarray(nums) == 1


def test_large_range_of_values() -> None:
    soln = Solution()
    nums = [2**i for i in range(20)]
    assert soln.longestSubarray(nums) == 1


if __name__ == "__main__":
    pytest.main()
