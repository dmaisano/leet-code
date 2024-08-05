import pytest

from .integer_to_english_words import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_number_to_words_0(solution: Solution) -> None:
    assert solution.numberToWords(0) == "Zero"


def test_number_to_words_1(solution: Solution) -> None:
    assert solution.numberToWords(1) == "One"


def test_number_to_words_15(solution: Solution) -> None:
    assert solution.numberToWords(15) == "Fifteen"


def test_number_to_words_23(solution: Solution) -> None:
    assert solution.numberToWords(23) == "Twenty Three"


def test_number_to_words_100(solution: Solution) -> None:
    assert solution.numberToWords(100) == "One Hundred"


def test_number_to_words_123(solution: Solution) -> None:
    assert solution.numberToWords(123) == "One Hundred Twenty Three"


def test_number_to_words_12345(solution: Solution) -> None:
    assert solution.numberToWords(12345) == "Twelve Thousand Three Hundred Forty Five"


def test_number_to_words_1234567(solution: Solution) -> None:
    assert (
        solution.numberToWords(1234567)
        == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    )


def test_number_to_words_1234567891(solution: Solution) -> None:
    assert (
        solution.numberToWords(1234567891)
        == "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
    )


def test_number_to_words_negative(solution: Solution) -> None:
    with pytest.raises(ValueError):
        solution.numberToWords(-1)


def test_number_to_words_large_number(solution: Solution) -> None:
    assert (
        solution.numberToWords(9876543210)
        == "Nine Billion Eight Hundred Seventy Six Million Five Hundred Forty Three Thousand Two Hundred Ten"
    )
