import pytest

from ..distribute_candies import Solution


@pytest.fixture
def soln() -> Solution:
    return Solution()


def test_distributeCandies(soln: Solution) -> None:
    assert soln.distributeCandies([1, 1, 2, 2, 3, 3]) == 3
    assert soln.distributeCandies([1, 1, 2, 3]) == 2
    assert soln.distributeCandies([6, 6, 6, 6]) == 1
    assert soln.distributeCandies([1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5]) == 5
    assert soln.distributeCandies([1, 2, 3, 4, 5, 6, 7, 8]) == 4
    assert soln.distributeCandies([1, 1, 1, 1, 2, 2, 2, 2]) == 2
    assert soln.distributeCandies([1, 2, 3, 3, 2, 1, 1, 1, 1, 1]) == 3


if __name__ == "__main__":
    pytest.main()