import pytest
from .jewels_and_stones import Solution


@pytest.fixture
def solution() -> Solution:
    return Solution()


def test_numJewelsInStones(soln: Solution) -> None:
    assert solution.numJewelsInStones("aA", "aAAbbbb") == 3
    assert solution.numJewelsInStones("z", "ZZ") == 0
    assert solution.numJewelsInStones("", "aAAbbbb") == 0
    assert solution.numJewelsInStones("aA", "") == 0
    assert solution.numJewelsInStones("aA", "aAaA") == 4
    assert solution.numJewelsInStones("abc", "aAbBcC") == 3
    assert solution.numJewelsInStones("a", "aaa") == 3


if __name__ == "__main__":
    pytest.main()
