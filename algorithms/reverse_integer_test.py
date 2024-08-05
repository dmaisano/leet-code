import pytest

from .reverse_integer import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_reverse_integer(solution: Solution) -> None:
    assert solution.reverse(123) == 321
    assert solution.reverse(-123) == -321
    assert solution.reverse(120) == 21
    assert solution.reverse(0) == 0
