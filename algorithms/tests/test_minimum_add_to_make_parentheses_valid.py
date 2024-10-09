import pytest

from algorithms.minimum_add_to_make_parentheses_valid import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_min_add_to_make_valid_empty_string(solution: Solution) -> None:
    assert solution.minAddToMakeValid("") == 0


def test_min_add_to_make_valid_no_additional_needed(solution: Solution) -> None:
    assert solution.minAddToMakeValid("()") == 0


def test_min_add_to_make_valid_one_additional_needed(solution: Solution) -> None:
    assert solution.minAddToMakeValid("(") == 1
    assert solution.minAddToMakeValid(")") == 1


def test_min_add_to_make_valid_mixed(solution: Solution) -> None:
    assert solution.minAddToMakeValid("())") == 1
    assert solution.minAddToMakeValid("(((") == 3
    assert solution.minAddToMakeValid("(()))(") == 2


def test_min_add_to_make_valid_complex(solution: Solution) -> None:
    assert solution.minAddToMakeValid("((())") == 1
    assert solution.minAddToMakeValid("())(()") == 2
    assert solution.minAddToMakeValid("()(()))(") == 2


if __name__ == "__main__":
    pytest.main()
