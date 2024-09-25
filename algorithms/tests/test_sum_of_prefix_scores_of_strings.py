import pytest
from algorithms.sum_of_prefix_scores_of_strings import Solution


def test_sumPrefixScores() -> None:
    solution = Solution()

    words = ["abc", "ab", "bc", "b"]
    expected = [5, 4, 3, 2]
    assert solution.sumPrefixScores(words) == expected

    words = ["abcd"]
    expected = [4]
    assert solution.sumPrefixScores(words) == expected

    words = ["a", "aa", "aaa", "aaaa"]
    expected = [4, 7, 9, 10]
    assert solution.sumPrefixScores(words) == expected

    words = ["x", "xy", "xyz", "xyzz"]
    expected = [4, 7, 9, 10]
    assert solution.sumPrefixScores(words) == expected

    words = ["a"]
    expected = [1]
    assert solution.sumPrefixScores(words) == expected

    words = ["a"] * 1000
    expected = [1000] * 1000
    assert solution.sumPrefixScores(words) == expected


if __name__ == "__main__":
    pytest.main()
