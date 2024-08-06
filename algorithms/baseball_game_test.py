import pytest
from .baseball_game import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_calPoints(solution: Solution) -> None:
    assert solution.calPoints(["5", "2", "C", "D", "+"]) == 30
    assert solution.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27
    assert solution.calPoints(["1", "C"]) == 0
    assert solution.calPoints([]) == 0
    assert solution.calPoints(["10"]) == 10
    assert solution.calPoints(["10", "C"]) == 0
    assert solution.calPoints(["5", "6", "D", "+", "C", "7", "D", "+"]) == 65
    assert solution.calPoints(["-5", "-10", "+", "D"]) == -60
    assert solution.calPoints(["10000", "20000", "+", "D"]) == 120000
    assert solution.calPoints(["8", "9", "C", "D", "+"]) == 48


if __name__ == "__main__":
    pytest.main()
