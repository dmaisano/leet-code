import pytest

from ..merge_strings_alternately import Solution


def test_merge_alternately_basic_case() -> None:
    solution = Solution()
    assert solution.mergeAlternately("abc", "pqr") == "apbqcr"


def test_merge_alternately_different_lengths() -> None:
    solution = Solution()
    assert solution.mergeAlternately("ab", "pqrs") == "apbqrs"
    assert solution.mergeAlternately("abcd", "pq") == "apbqcd"


def test_merge_alternately_empty_strings() -> None:
    solution = Solution()
    assert solution.mergeAlternately("", "") == ""
    assert solution.mergeAlternately("abc", "") == "abc"
    assert solution.mergeAlternately("", "pqr") == "pqr"


def test_merge_alternately_one_char_strings() -> None:
    solution = Solution()
    assert solution.mergeAlternately("a", "b") == "ab"
    assert solution.mergeAlternately("a", "") == "a"
    assert solution.mergeAlternately("", "b") == "b"


def test_merge_alternately_long_strings() -> None:
    solution = Solution()
    assert solution.mergeAlternately("abcdefg", "hijklmn") == "ahbicjdkelfmgn"


if __name__ == "__main__":
    pytest.main()
