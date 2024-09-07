import pytest

from ..valid_parentheses import Solution


def test_valid_parentheses() -> None:
    assert Solution().isValid("()") == True
    assert Solution().isValid("()[]{}") == True
    assert Solution().isValid("{[]}") == True


def test_invalid_parentheses() -> None:
    assert Solution().isValid("(]") == False
    assert Solution().isValid("([)]") == False
    assert Solution().isValid("(((()") == False


def test_empty_string() -> None:
    assert Solution().isValid("") == True


def test_single_parenthesis() -> None:
    assert Solution().isValid("(") == False
    assert Solution().isValid(")") == False


def test_nested_parentheses() -> None:
    assert Solution().isValid("((()))") == True
    assert Solution().isValid("{[()]}") == True


def test_unbalanced_long_string() -> None:
    assert Solution().isValid("(((()))){{}}") == True
    assert Solution().isValid("(((((()") == False


if __name__ == "__main__":
    pytest.main()
