import pytest

from .integer_to_roman import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_int_to_roman_1(solution: Solution) -> None:
    assert solution.intToRoman(1) == "I"


def test_int_to_roman_4(solution: Solution) -> None:
    assert solution.intToRoman(4) == "IV"


def test_int_to_roman_9(solution: Solution) -> None:
    assert solution.intToRoman(9) == "IX"


def test_int_to_roman_58(solution: Solution) -> None:
    assert solution.intToRoman(58) == "LVIII"


def test_int_to_roman_1994(solution: Solution) -> None:
    assert solution.intToRoman(1994) == "MCMXCIV"


def test_int_to_roman_3999(solution: Solution) -> None:
    assert solution.intToRoman(3999) == "MMMCMXCIX"


def test_int_to_roman_0(solution: Solution) -> None:
    assert solution.intToRoman(0) == ""


def test_int_to_roman_edge_cases(solution: Solution) -> None:
    assert solution.intToRoman(3999) == "MMMCMXCIX"
    assert solution.intToRoman(1) == "I"


if __name__ == "__main__":
    pytest.main()
