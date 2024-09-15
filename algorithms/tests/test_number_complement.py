import pytest

from algorithms.number_complement import Solution


def test_find_complement_example_1() -> None:
    sol = Solution()
    assert sol.findComplement(5) == 2


def test_find_complement_example_2() -> None:
    sol = Solution()
    assert sol.findComplement(1) == 0


def test_find_complement_small_number() -> None:
    sol = Solution()
    assert sol.findComplement(2) == 1


def test_find_complement_large_number() -> None:
    sol = Solution()
    assert sol.findComplement(1023) == 0


def test_find_complement_power_of_two() -> None:
    sol = Solution()
    assert sol.findComplement(16) == 15


def test_find_complement_all_ones() -> None:
    sol = Solution()
    assert sol.findComplement(7) == 0


def test_find_complement_maximum_integer() -> None:
    sol = Solution()
    assert sol.findComplement(2**30) == 2**30 - 1


if __name__ == "__main__":
    pytest.main()
