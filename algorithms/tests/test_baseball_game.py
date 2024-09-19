import pytest

from algorithms.baseball_game import Solution


def test_calPoints() -> None:
    soln = Solution()
    assert soln.calPoints(["5", "2", "C", "D", "+"]) == 30
    assert soln.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27
    assert soln.calPoints(["1", "C"]) == 0
    assert soln.calPoints([]) == 0
    assert soln.calPoints(["10"]) == 10
    assert soln.calPoints(["10", "C"]) == 0
    assert soln.calPoints(["5", "6", "D", "+", "C", "7", "D", "+"]) == 65
    assert soln.calPoints(["-5", "-10", "+", "D"]) == -60
    assert soln.calPoints(["10000", "20000", "+", "D"]) == 120000
    assert soln.calPoints(["8", "9", "C", "D", "+"]) == 48


if __name__ == "__main__":
    pytest.main()
