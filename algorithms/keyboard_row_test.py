from typing import List

import pytest

from .keyboard_row import Solution


@pytest.fixture
def soln() -> Solution:
    return Solution()


def test_findWords_with_all_row1_words(soln: Solution) -> None:
    words = ["not_row_1", "also_not_row_1", "def_not_row_1", "QwErTy"]
    expected = ["QwErTy"]
    print(soln.findWords(words))
    assert soln.findWords(words) == expected


def test_findWords_with_all_row2_words(soln: Solution) -> None:
    words = ["asdf", "Sdfgh", "jkL"]
    expected = ["asdf", "Sdfgh", "jkL"]
    assert soln.findWords(words) == expected


def test_findWords_with_all_row3_words(soln: Solution) -> None:
    words = ["zxcvb", "mnbvcxz", "ZZX"]
    expected = ["zxcvb", "mnbvcxz", "ZZX"]
    assert soln.findWords(words) == expected


def test_findWords_with_mixed_row_words(soln: Solution) -> None:
    words = ["Hello", "World", "Python", "QwErTy"]
    expected = ["QwErTy"]
    assert soln.findWords(words) == expected


def test_findWords_with_empty_list(soln: Solution) -> None:
    words: List[str] = []
    expected: List[str] = []
    assert soln.findWords(words) == expected


def test_findWords_with_no_valid_words(soln: Solution) -> None:
    words = ["Hello", "World", "Peace"]
    expected: List[str] = []
    assert soln.findWords(words) == expected


def test_findWords_with_single_row_words(soln: Solution) -> None:
    words = ["Qwerty", "asdfg", "zxcvb", "Dad", "Alaska", "Peace"]
    expected = ["Qwerty", "asdfg", "zxcvb", "Dad", "Alaska"]
    assert soln.findWords(words) == expected


def test_findWords_with_case_insensitivity(soln: Solution) -> None:
    words = ["QWERTY", "ASDFG", "ZXCVB", "QwErTy"]
    expected = ["QWERTY", "ASDFG", "ZXCVB", "QwErTy"]
    assert soln.findWords(words) == expected


if __name__ == "__main__":
    pytest.main()
