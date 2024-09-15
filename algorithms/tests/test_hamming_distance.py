import pytest

from algorithms.hamming_distance import Solution


def test_hamming_distance_example_1() -> None:
    sol = Solution()
    assert sol.hammingDistance(1, 4) == 2


def test_hamming_distance_example_2() -> None:
    sol = Solution()
    assert sol.hammingDistance(3, 1) == 1


def test_hamming_distance_zero() -> None:
    sol = Solution()
    assert sol.hammingDistance(0, 0) == 0


def test_hamming_distance_same_number() -> None:
    sol = Solution()
    assert sol.hammingDistance(5, 5) == 0


def test_hamming_distance_power_of_two() -> None:
    sol = Solution()
    assert sol.hammingDistance(2**10, 2**15) == 2


def test_hamming_distance_maximum_integer() -> None:
    sol = Solution()
    assert sol.hammingDistance(2**31 - 1, 0) == 31


if __name__ == "__main__":
    pytest.main()
