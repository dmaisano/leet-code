import pytest

from .partitioning_into_minimum_number_of_deci_binary_numbers import Solution


@pytest.fixture
def soln() -> Solution:
    return Solution()


def test_min_partitions_all_same_digits(soln: Solution) -> None:
    assert soln.minPartitions("111") == 1
    assert soln.minPartitions("999") == 9


def test_min_partitions_different_digits(soln: Solution) -> None:
    assert soln.minPartitions("32") == 3
    assert soln.minPartitions("82734") == 8
    assert soln.minPartitions("27346209830709182346") == 9


def test_min_partitions_single_digit(soln: Solution) -> None:
    assert soln.minPartitions("0") == 0
    assert soln.minPartitions("1") == 1
    assert soln.minPartitions("5") == 5


def test_min_partitions_leading_zeros(soln: Solution) -> None:
    assert soln.minPartitions("00032") == 3
    assert soln.minPartitions("00789") == 9


def test_min_partitions_large_number(soln: Solution) -> None:
    assert soln.minPartitions("12345678901234567890") == 9


def test_min_partitions_empty_string(soln: Solution) -> None:
    with pytest.raises(ValueError):
        soln.minPartitions("")


def test_min_partitions_non_numeric_characters(soln: Solution) -> None:
    with pytest.raises(ValueError):
        soln.minPartitions("12a34")


if __name__ == "__main__":
    pytest.main()
