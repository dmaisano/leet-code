import pytest

from ..reverse_integer import Solution


@pytest.fixture
def soln() -> Solution:
    return Solution()


def test_reverse_integer(soln: Solution) -> None:
    assert soln.reverse(123) == 321
    assert soln.reverse(-123) == -321
    assert soln.reverse(120) == 21
    assert soln.reverse(0) == 0


if __name__ == "__main__":
    pytest.main()
