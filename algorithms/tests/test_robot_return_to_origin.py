import pytest

from algorithms.robot_return_to_origin import Solution


def test_judgeCircle() -> None:
    soln = Solution()
    assert soln.judgeCircle("UD") == True, "Test case 1 failed"
    assert soln.judgeCircle("LL") == False, "Test case 2 failed"
    assert soln.judgeCircle("") == True, "Test case 3 failed"
    assert soln.judgeCircle("LRUD") == True, "Test case 4 failed"
    assert soln.judgeCircle("RRDDLUU") == False, "Test case 5 failed"


if __name__ == "__main__":
    pytest.main()
