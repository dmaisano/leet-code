import pytest

from algorithms.max_consecutive_ones import Solution


@pytest.fixture
def soln() -> Solution:
    return Solution()


def test_empty_list(soln: Solution) -> None:
    assert soln.findMaxConsecutiveOnes([]) == 0


def test_single_zero(soln: Solution) -> None:
    assert soln.findMaxConsecutiveOnes([0]) == 0


def test_single_one(soln: Solution) -> None:
    assert soln.findMaxConsecutiveOnes([1]) == 1


def test_mixed_values(soln: Solution) -> None:
    assert soln.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3


def test_all_ones(soln: Solution) -> None:
    assert soln.findMaxConsecutiveOnes([1, 1, 1, 1]) == 4


def test_all_zeros(soln: Solution) -> None:
    assert soln.findMaxConsecutiveOnes([0, 0, 0, 0]) == 0


def test_leading_and_trailing_zeros(soln: Solution) -> None:
    assert soln.findMaxConsecutiveOnes([0, 1, 1, 0, 1, 1, 1, 0]) == 3


def test_alternating_ones_and_zeros(soln: Solution) -> None:
    assert soln.findMaxConsecutiveOnes([1, 0, 1, 0, 1, 0, 1]) == 1


if __name__ == "__main__":
    pytest.main()
