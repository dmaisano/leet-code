import pytest

from algorithms.fibonacci_number import Solution


@pytest.fixture
def soln() -> Solution:
    return Solution()


def test_fib_zero(soln: Solution) -> None:
    assert soln.fib(0) == 0


def test_fib_one(soln: Solution) -> None:
    assert soln.fib(1) == 1


def test_fib_two(soln: Solution) -> None:
    assert soln.fib(2) == 1


def test_fib_three(soln: Solution) -> None:
    assert soln.fib(3) == 2


def test_fib_ten(soln: Solution) -> None:
    assert soln.fib(10) == 55


def test_fib_negative(soln: Solution) -> None:
    with pytest.raises(ValueError, match="n must be a non-negative integer"):
        soln.fib(-1)


def test_fib_large(soln: Solution) -> None:
    assert soln.fib(30) == 832040


def test_cache(soln: Solution) -> None:
    soln.cache = {0: 0, 1: 1}  # Reset cache to initial state
    soln.fib(10)
    assert soln.cache[10] == 55
    assert soln.cache[9] == 34
    assert soln.cache[8] == 21


if __name__ == "__main__":
    pytest.main()
