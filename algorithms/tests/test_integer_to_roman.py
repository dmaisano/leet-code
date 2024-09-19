import pytest

from algorithms.integer_to_roman import Solution


def test_int_to_roman_1() -> None:
    soln = Solution()
    assert soln.intToRoman(1) == "I"


def test_int_to_roman_4() -> None:
    soln = Solution()
    assert soln.intToRoman(4) == "IV"


def test_int_to_roman_9() -> None:
    soln = Solution()
    assert soln.intToRoman(9) == "IX"


def test_int_to_roman_58() -> None:
    soln = Solution()
    assert soln.intToRoman(58) == "LVIII"


def test_int_to_roman_1994() -> None:
    soln = Solution()
    assert soln.intToRoman(1994) == "MCMXCIV"


def test_int_to_roman_3999() -> None:
    soln = Solution()
    assert soln.intToRoman(3999) == "MMMCMXCIX"


def test_int_to_roman_0() -> None:
    soln = Solution()
    assert soln.intToRoman(0) == ""


def test_int_to_roman_edge_cases() -> None:
    soln = Solution()
    assert soln.intToRoman(3999) == "MMMCMXCIX"
    assert soln.intToRoman(1) == "I"


if __name__ == "__main__":
    pytest.main()
