import pytest

from hackerrank.first_unique_character import getUniqueCharacter


def test_getUniqueCharacter() -> None:
    # Test cases where unique character exists
    assert getUniqueCharacter("hackthegame") == 3
    assert getUniqueCharacter("swiss") == 2
    assert getUniqueCharacter("character") == 2

    # Test cases where unique character does not exist
    assert getUniqueCharacter("aabbcc") == -1
    assert getUniqueCharacter("aabb") == -1

    # Test case with single character string
    assert getUniqueCharacter("z") == 1

    # Test case with empty string
    assert getUniqueCharacter("") == -1

    # Test case with all characters unique
    assert getUniqueCharacter("abcdef") == 1


if __name__ == "__main__":
    pytest.main()
