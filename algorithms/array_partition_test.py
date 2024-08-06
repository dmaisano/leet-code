import pytest

from .array_partition import Solution


@pytest.fixture
def soln() -> Solution:
    return Solution()


def test_arrayPairSum(soln: Solution) -> None:
    assert soln.arrayPairSum([1, 4, 3, 2]) == 4
    assert soln.arrayPairSum([6, 2, 6, 5, 1, 2]) == 9
    assert soln.arrayPairSum([1, 1, 1, 1]) == 2
    assert soln.arrayPairSum([-1, -2, -3, -4]) == -6
    assert soln.arrayPairSum([1, 2, 3, 4, 5, 6]) == 9
    assert soln.arrayPairSum([7, 3, 1, 0, 0, 6]) == 7
    assert soln.arrayPairSum([-5, -3, -2, -1, 2, 4]) == -5
    assert soln.arrayPairSum([10, 10, 10, 10]) == 20


if __name__ == "__main__":
    pytest.main()
