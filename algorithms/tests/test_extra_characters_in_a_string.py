import pytest

from algorithms.extra_characters_in_a_string import Solution


def test_example_1() -> None:
    s = "leetscode"
    dictionary = ["leet", "code", "leetcode"]
    assert Solution().minExtraChar(s, dictionary) == 1


def test_example_2() -> None:
    s = "sayhelloworld"
    dictionary = ["hello", "world"]
    assert Solution().minExtraChar(s, dictionary) == 3


def test_single_word_in_dict() -> None:
    s = "leetcode"
    dictionary = ["leetcode"]
    assert Solution().minExtraChar(s, dictionary) == 0


def test_no_matching_word() -> None:
    s = "abcdef"
    dictionary = ["ghijk"]
    assert Solution().minExtraChar(s, dictionary) == len(s)


def test_all_characters_extra() -> None:
    s = "abcdefgh"
    dictionary: list[str] = []
    assert Solution().minExtraChar(s, dictionary) == len(s)


def test_substring_overlap() -> None:
    s = "leetcodeleet"
    dictionary = ["leet", "code"]
    assert Solution().minExtraChar(s, dictionary) == 0


def test_large_input() -> None:
    s = "x" * 50
    dictionary = ["x" * 49]
    assert Solution().minExtraChar(s, dictionary) == 1


def test_partial_match() -> None:
    s = "abcxyzabc"
    dictionary = ["abc", "xyz"]
    assert Solution().minExtraChar(s, dictionary) == 0


def test_only_partial_substrings() -> None:
    s = "partofstring"
    dictionary = ["part", "string"]
    assert Solution().minExtraChar(s, dictionary) == 2  # 'of' remains extra


if __name__ == "__main__":
    pytest.main()
