from typing import List

import pytest

from algorithms.different_ways_to_add_parentheses import Solution


@pytest.fixture
def soln() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "expression, expected_outputs",
    [
        ("2-1-1", [0, 2]),
        ("2*3-4*5", [-34, -14, -10, -10, 10]),
        ("10+5", [15]),
        (
            "2*3-4*5+1",
            [-42, -36, -33, -32, -18, -15, -13, -12, -12, -9, -9, -8, 11, 12],
        ),
        ("", []),
        ("5", [5]),
        ("2+3*2", [10, 8]),
    ],
)
def test_diffWaysToCompute(expression: str, expected_outputs: List[int]) -> None:
    solution = Solution()
    result = solution.diffWaysToCompute(expression)
    assert sorted(result) == sorted(
        expected_outputs
    ), f"Failed for expression: {expression}"


if __name__ == "__main__":
    pytest.main()
