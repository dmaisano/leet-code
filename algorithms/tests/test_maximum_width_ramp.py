import pytest

from algorithms.maximum_width_ramp import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_max_width_ramp_case_1(solution: Solution) -> None:
    nums = [6, 0, 8, 2, 1, 5]
    assert solution.maxWidthRamp(nums) == 4


def test_max_width_ramp_case_2(solution: Solution) -> None:
    nums = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]
    assert solution.maxWidthRamp(nums) == 7


def test_max_width_ramp_case_3(solution: Solution) -> None:
    nums = [1, 2, 3, 4, 5]
    assert solution.maxWidthRamp(nums) == 4


def test_max_width_ramp_case_4(solution: Solution) -> None:
    nums = [5, 4, 3, 2, 1]
    assert solution.maxWidthRamp(nums) == 0


def test_max_width_ramp_case_5(solution: Solution) -> None:
    nums = [1, 1, 1, 1, 1]
    assert solution.maxWidthRamp(nums) == 4


if __name__ == "__main__":
    pytest.main()
