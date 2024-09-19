import pytest

from algorithms.integer_to_english_words import Solution


def test_number_to_words_0() -> None:
    soln = Solution()
    assert soln.numberToWords(0) == "Zero"


def test_number_to_words_1() -> None:
    soln = Solution()
    assert soln.numberToWords(1) == "One"


def test_number_to_words_15() -> None:
    soln = Solution()
    assert soln.numberToWords(15) == "Fifteen"


def test_number_to_words_23() -> None:
    soln = Solution()
    assert soln.numberToWords(23) == "Twenty Three"


def test_number_to_words_100() -> None:
    soln = Solution()
    assert soln.numberToWords(100) == "One Hundred"


def test_number_to_words_123() -> None:
    soln = Solution()
    assert soln.numberToWords(123) == "One Hundred Twenty Three"


def test_number_to_words_12345() -> None:
    soln = Solution()
    assert soln.numberToWords(12345) == "Twelve Thousand Three Hundred Forty Five"


def test_number_to_words_1234567() -> None:
    soln = Solution()
    assert (
        soln.numberToWords(1234567)
        == "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    )


def test_number_to_words_1234567891() -> None:
    soln = Solution()
    assert (
        soln.numberToWords(1234567891)
        == "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
    )


def test_number_to_words_negative() -> None:
    soln = Solution()
    with pytest.raises(ValueError):
        soln.numberToWords(-1)


def test_number_to_words_large_number() -> None:
    soln = Solution()
    assert (
        soln.numberToWords(9876543210)
        == "Nine Billion Eight Hundred Seventy Six Million Five Hundred Forty Three Thousand Two Hundred Ten"
    )


if __name__ == "__main__":
    pytest.main()
