import pytest

from algorithms.max_consecutive_ones import Solution


def test_empty_list() -> None:
    soln = Solution()
    assert soln.findMaxConsecutiveOnes([]) == 0


def test_single_zero() -> None:
    soln = Solution()
    assert soln.findMaxConsecutiveOnes([0]) == 0


def test_single_one() -> None:
    soln = Solution()
    assert soln.findMaxConsecutiveOnes([1]) == 1


def test_mixed_values() -> None:
    soln = Solution()
    assert soln.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3


def test_all_ones() -> None:
    soln = Solution()
    assert soln.findMaxConsecutiveOnes([1, 1, 1, 1]) == 4


def test_all_zeros() -> None:
    soln = Solution()
    assert soln.findMaxConsecutiveOnes([0, 0, 0, 0]) == 0


def test_leading_and_trailing_zeros() -> None:
    soln = Solution()
    assert soln.findMaxConsecutiveOnes([0, 1, 1, 0, 1, 1, 1, 0]) == 3


def test_alternating_ones_and_zeros() -> None:
    soln = Solution()
    assert soln.findMaxConsecutiveOnes([1, 0, 1, 0, 1, 0, 1]) == 1


if __name__ == "__main__":
    pytest.main()
