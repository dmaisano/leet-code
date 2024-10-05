import pytest
from algorithms.permutation_in_string import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_check_inclusion_true_case(solution: Solution) -> None:
    assert solution.checkInclusion("ab", "eidbaooo") == True


def test_check_inclusion_false_case(solution: Solution) -> None:
    assert solution.checkInclusion("ab", "eidboaoo") == False


def test_check_inclusion_empty_s1(solution: Solution) -> None:
    assert solution.checkInclusion("", "anything") == True


def test_check_inclusion_empty_s2(solution: Solution) -> None:
    assert solution.checkInclusion("a", "") == False


def test_check_inclusion_s1_longer_than_s2(solution: Solution) -> None:
    assert solution.checkInclusion("longstring", "short") == False


def test_check_inclusion_identical_strings(solution: Solution) -> None:
    assert solution.checkInclusion("abc", "abc") == True


def test_check_inclusion_no_permutation(solution: Solution) -> None:
    assert solution.checkInclusion("abc", "defghijkl") == False


def test_check_inclusion_permutation_at_end(solution: Solution) -> None:
    assert solution.checkInclusion("abc", "defghijklabc") == True


if __name__ == "__main__":
    pytest.main()
