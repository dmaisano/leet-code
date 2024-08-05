import pytest

from .partitioning_into_minimum_number_of_deci_binary_numbers import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_min_partitions_all_same_digits(solution: Solution) -> None:
    assert solution.minPartitions("111") == 1
    assert solution.minPartitions("999") == 9


def test_min_partitions_different_digits(solution: Solution) -> None:
    assert solution.minPartitions("32") == 3
    assert solution.minPartitions("82734") == 8
    assert solution.minPartitions("27346209830709182346") == 9


def test_min_partitions_single_digit(solution: Solution) -> None:
    assert solution.minPartitions("0") == 0
    assert solution.minPartitions("1") == 1
    assert solution.minPartitions("5") == 5


def test_min_partitions_leading_zeros(solution: Solution) -> None:
    assert solution.minPartitions("00032") == 3
    assert solution.minPartitions("00789") == 9


def test_min_partitions_large_number(solution: Solution) -> None:
    assert solution.minPartitions("12345678901234567890") == 9


def test_min_partitions_empty_string(solution: Solution) -> None:
    with pytest.raises(ValueError):
        solution.minPartitions("")


def test_min_partitions_non_numeric_characters(solution: Solution) -> None:
    with pytest.raises(ValueError):
        solution.minPartitions("12a34")
