import pytest
from algorithms.rank_transform_of_an_array import Solution


def test_arrayRankTransform_empty() -> None:
    sol = Solution()
    assert sol.arrayRankTransform([]) == []


def test_arrayRankTransform_single_element() -> None:
    sol = Solution()
    assert sol.arrayRankTransform([100]) == [1]


def test_arrayRankTransform_sorted() -> None:
    sol = Solution()
    assert sol.arrayRankTransform([10, 20, 30]) == [1, 2, 3]


def test_arrayRankTransform_unsorted() -> None:
    sol = Solution()
    assert sol.arrayRankTransform([40, 10, 20, 30]) == [4, 1, 2, 3]


def test_arrayRankTransform_with_duplicates() -> None:
    sol = Solution()
    assert sol.arrayRankTransform([100, 100, 100]) == [1, 1, 1]


def test_arrayRankTransform_mixed() -> None:
    sol = Solution()
    assert sol.arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]) == [
        5,
        3,
        4,
        2,
        8,
        6,
        7,
        1,
        3,
    ]


if __name__ == "__main__":
    pytest.main()
