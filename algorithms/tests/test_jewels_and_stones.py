import pytest

from algorithms.jewels_and_stones import Solution


def test_numJewelsInStones() -> None:
    soln = Solution()
    assert soln.numJewelsInStones("aA", "aAAbbbb") == 3
    assert soln.numJewelsInStones("z", "ZZ") == 0
    assert soln.numJewelsInStones("", "aAAbbbb") == 0
    assert soln.numJewelsInStones("aA", "") == 0
    assert soln.numJewelsInStones("aA", "aAaA") == 4
    assert soln.numJewelsInStones("abc", "aAbBcC") == 3
    assert soln.numJewelsInStones("a", "aaa") == 3


if __name__ == "__main__":
    pytest.main()
