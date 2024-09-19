from typing import List

import pytest

from algorithms.keyboard_row import Solution


def test_findWords_with_all_row1_words() -> None:
    soln = Solution()
    words = ["not_row_1", "also_not_row_1", "def_not_row_1", "QwErTy"]
    expected = ["QwErTy"]
    assert soln.findWords(words) == expected


def test_findWords_with_all_row2_words() -> None:
    soln = Solution()
    words = ["asdf", "Sdfgh", "jkL"]
    expected = ["asdf", "Sdfgh", "jkL"]
    assert soln.findWords(words) == expected


def test_findWords_with_all_row3_words() -> None:
    soln = Solution()
    words = ["zxcvb", "mnbvcxz", "ZZX"]
    expected = ["zxcvb", "mnbvcxz", "ZZX"]
    assert soln.findWords(words) == expected


def test_findWords_with_mixed_row_words() -> None:
    soln = Solution()
    words = ["Hello", "World", "Python", "QwErTy"]
    expected = ["QwErTy"]
    assert soln.findWords(words) == expected


def test_findWords_with_empty_list() -> None:
    soln = Solution()
    words: List[str] = []
    expected: List[str] = []
    assert soln.findWords(words) == expected


def test_findWords_with_no_valid_words() -> None:
    soln = Solution()
    words = ["Hello", "World", "Peace"]
    expected: List[str] = []
    assert soln.findWords(words) == expected


def test_findWords_with_single_row_words() -> None:
    soln = Solution()
    words = ["Qwerty", "asdfg", "zxcvb", "Dad", "Alaska", "Peace"]
    expected = ["Qwerty", "asdfg", "zxcvb", "Dad", "Alaska"]
    assert soln.findWords(words) == expected


def test_findWords_with_case_insensitivity() -> None:
    soln = Solution()
    words = ["QWERTY", "ASDFG", "ZXCVB", "QwErTy"]
    expected = ["QWERTY", "ASDFG", "ZXCVB", "QwErTy"]
    assert soln.findWords(words) == expected


if __name__ == "__main__":
    pytest.main()
