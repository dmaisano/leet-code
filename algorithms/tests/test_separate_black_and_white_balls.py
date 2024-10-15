import pytest
from algorithms.separate_black_and_white_balls import Solution


def test_minimum_steps() -> None:
    solution = Solution()
    assert solution.minimumSteps("110") == 2
    assert solution.minimumSteps("1001") == 2
    assert solution.minimumSteps("111") == 0
    assert solution.minimumSteps("000") == 0
    assert solution.minimumSteps("101010") == 6
    assert solution.minimumSteps("1100") == 4
    assert solution.minimumSteps("") == 0
    assert solution.minimumSteps("1") == 0
    assert solution.minimumSteps("0") == 0


if __name__ == "__main__":
    pytest.main()
