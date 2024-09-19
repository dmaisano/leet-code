import pytest

from algorithms.reverse_integer import Solution


def test_reverse_integer() -> None:
    soln = Solution()
    assert soln.reverse(123) == 321
    assert soln.reverse(-123) == -321
    assert soln.reverse(120) == 21
    assert soln.reverse(0) == 0


if __name__ == "__main__":
    pytest.main()
