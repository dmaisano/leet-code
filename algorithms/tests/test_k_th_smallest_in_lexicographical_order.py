import pytest
from algorithms.k_th_smallest_in_lexicographical_order import Solution


def test_example_1() -> None:
    assert Solution().findKthNumber(13, 2) == 10


def test_example_2() -> None:
    assert Solution().findKthNumber(1, 1) == 1


def test_small_range() -> None:
    assert (
        Solution().findKthNumber(9, 5) == 5
    )  # The numbers are [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_large_range_middle() -> None:
    assert (
        Solution().findKthNumber(100, 10) == 17
    )  # The lexicographical order is [1, 10, 11, ..., 17, ..., 99, 100]


def test_large_n_k() -> None:
    assert Solution().findKthNumber(1000000, 1000) == 100896


def test_edge_case_k_equals_n() -> None:

    assert Solution().findKthNumber(10, 10) == 9


def test_edge_case_n_large_k_small() -> None:
    assert Solution().findKthNumber(1000000000, 1) == 1


if __name__ == "__main__":
    pytest.main()
