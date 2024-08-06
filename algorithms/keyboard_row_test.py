import pytest

from .keyboard_row import Solution


@pytest.fixture
def soln() -> Solution:
    return Solution()


def test_case_1(soln: Solution) -> None:
    words = ["Hello", "Alaska", "Dad", "Peace"]
    expected = ["Alaska", "Dad"]
    assert soln.findWords(words) == expected


def test_case_2(soln: Solution) -> None:
    words = ["omk"]
    expected: list[str] = []
    assert soln.findWords(words) == expected


def test_case_3(soln: Solution) -> None:
    words = ["adsdf", "sfd"]
    expected = ["adsdf", "sfd"]
    assert soln.findWords(words) == expected


def test_case_4(soln: Solution) -> None:
    words = ["qwerty", "asdf", "zxcvbn", "pop"]
    expected = ["qwerty", "asdf", "zxcvbn", "pop"]
    assert soln.findWords(words) == expected


def test_case_5(soln: Solution) -> None:
    words = ["QwErTyUiOp", "ASDFGHJKL", "ZXCVBNM"]
    expected = ["QwErTyUiOp", "ASDFGHJKL", "ZXCVBNM"]
    assert soln.findWords(words) == expected


def test_case_6(soln: Solution) -> None:
    words = ["Hello", "World"]
    expected: list[str] = []
    assert soln.findWords(words) == expected


def test_case_7(soln: Solution) -> None:
    words: list[str] = []
    expected: list[str] = []
    assert soln.findWords(words) == expected


def test_case_8(soln: Solution) -> None:
    words = ["QWER", "asdf", "zxcv", "tyuiop", "ghjkl", "bnm"]
    expected = ["QWER", "asdf", "zxcv", "tyuiop", "ghjkl", "bnm"]
    assert soln.findWords(words) == expected


if __name__ == "__main__":
    pytest.main()
