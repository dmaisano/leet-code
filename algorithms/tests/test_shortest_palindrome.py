import pytest

from algorithms.shortest_palindrome import Solution


@pytest.mark.parametrize(
    "input_str, expected_str",
    [
        ("aacecaaa", "aaacecaaa"),
        ("abcd", "dcbabcd"),
        ("racecar", "racecar"),
        ("", ""),
        ("a", "a"),
        ("ab", "bab"),
        ("abcba", "abcba"),
        ("aa", "aa"),
        ("aaaxaaax", "xaaaxaaax"),
    ],
)
def test_shortest_palindrome(input_str: str, expected_str: str) -> None:
    soln = Solution()
    assert soln.shortestPalindrome(input_str) == expected_str


if __name__ == "__main__":
    pytest.main()
