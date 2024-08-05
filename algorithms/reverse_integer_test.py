import pytest
from reverse_integer import Solution


def test_reverse_zero():
    assert Solution().reverse(0) == 0


def test_reverse_positive_integer():
    assert Solution().reverse(123) == 321


def test_reverse_negative_integer():
    assert Solution().reverse(-123) == -321


def test_reverse_positive_integer_out_of_32_bit_range():
    assert Solution().reverse(2147483648) == 0


def test_reverse_negative_integer_out_of_32_bit_range():
    assert Solution().reverse(-2147483649) == 0
