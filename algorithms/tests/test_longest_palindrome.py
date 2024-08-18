import pytest

from ..longest_palindrome import Solution

soln = Solution()


def test_single_character() -> None:
    assert soln.longestPalindrome("a") == 1


def test_all_same_characters() -> None:
    assert soln.longestPalindrome("aaaa") == 4


def test_mixed_even_odd_characters() -> None:
    assert soln.longestPalindrome("abccccdd") == 7


def test_all_unique_characters() -> None:
    assert soln.longestPalindrome("abcdef") == 1


def test_multiple_odd_count_characters() -> None:
    assert soln.longestPalindrome("aaabbbccc") == 7


def test_empty_string() -> None:
    assert soln.longestPalindrome("") == 0


def test_palindrome_string() -> None:
    assert soln.longestPalindrome("abccba") == 6


def test_multiple_palindromes_possible() -> None:
    assert soln.longestPalindrome("abccccdd") == 7
    assert soln.longestPalindrome("abccbaabc") == 7


if __name__ == "__main__":
    pytest.main()
