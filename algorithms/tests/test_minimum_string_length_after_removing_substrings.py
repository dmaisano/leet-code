import pytest

from algorithms.minimum_string_length_after_removing_substrings import Solution


@pytest.mark.parametrize(
    "input_str, expected_length",
    [
        ("AB", 0),  # "AB" -> ""
        ("CD", 0),  # "CD" -> ""
        ("AABBCCDD", 0),  # "AABBCCDD" -> ""
        ("AABCCBD", 5),  # "AABCCBD" -> "ACCBD"
        ("ACBD", 4),  # "ACBD" -> "ACBD"
        ("", 0),  # Empty string
        ("A", 1),  # Single character
        ("B", 1),  # Single character
        ("C", 1),  # Single character
        ("D", 1),  # Single character
        ("ABCD", 0),  # "ABCD" -> ""
        ("ACBDAB", 4),  # "ACBDAB" -> "ACBD"
    ],
)
def test_min_length(input_str: str, expected_length: int) -> None:
    solution = Solution()
    assert solution.minLength(input_str) == expected_length


if __name__ == "__main__":
    pytest.main()
