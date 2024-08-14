from typing import List
import pytest

from ..items_in_containers import number_of_items


def test_single_compartment_with_items() -> None:
    s = "|**|"
    start_indices = [1]
    end_indices = [4]
    assert number_of_items(s, start_indices, end_indices) == [2]


def test_multiple_compartments() -> None:
    s = "|**|*|*"
    start_indices = [1, 1]
    end_indices = [5, 7]
    assert number_of_items(s, start_indices, end_indices) == [2, 3]


def test_no_compartments() -> None:
    s = "*|*|"
    start_indices = [1]
    end_indices = [3]
    assert number_of_items(s, start_indices, end_indices) == [0]


def test_single_item() -> None:
    s = "|*|"
    start_indices = [1]
    end_indices = [3]
    assert number_of_items(s, start_indices, end_indices) == [1]


def test_empty_string() -> None:
    s = ""
    start_indices: List[int] = []
    end_indices: List[int] = []
    assert number_of_items(s, start_indices, end_indices) == []


def test_no_items_between_pipes() -> None:
    s = "|*||*|"
    start_indices = [2]
    end_indices = [4]
    assert number_of_items(s, start_indices, end_indices) == [0]


def test_all_items_outside_compartments() -> None:
    s = "*|*|*|*"
    start_indices = [1]
    end_indices = [7]
    assert number_of_items(s, start_indices, end_indices) == [2]


def test_multiple_queries_with_different_results() -> None:
    s = "*|*|**|*"
    start_indices = [1, 2, 4, 5]
    end_indices = [8, 5, 7, 8]
    assert number_of_items(s, start_indices, end_indices) == [3, 1, 2, 0]


def test_start_and_end_same() -> None:
    s = "*|*|*"
    start_indices = [3]
    end_indices = [3]
    assert number_of_items(s, start_indices, end_indices) == [0]


if __name__ == "__main__":
    pytest.main()
