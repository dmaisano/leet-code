import pytest
from algorithms.minimum_number_of_swaps_to_make_the_string_balanced import Solution


@pytest.mark.parametrize(
    "s, expected",
    [
        ("[]", 0),
        ("][", 1),
        ("[[]]", 0),
        ("][][", 1),
        ("[[[[]]]]", 0),
        ("]]]][[[[", 2),
        ("[[][]]", 0),
        ("][]][[", 1),
    ],
)
def test_minSwaps(s: str, expected: int) -> None:
    solution = Solution()
    assert solution.minSwaps(s) == expected


if __name__ == "__main__":
    pytest.main()
