import pytest

from algorithms.divide_players_into_teams_of_equal_skill import Solution


def test_divide_players_equal_teams() -> None:
    solution = Solution()
    assert solution.dividePlayers([1, 2, 3, 4]) == 10
    assert solution.dividePlayers([1, 1, 2, 2]) == 4
    assert solution.dividePlayers([3, 6, 3, 6]) == 36


def test_divide_players_unequal_teams() -> None:
    solution = Solution()
    assert solution.dividePlayers([1, 1, 2, 3]) == -1
    assert solution.dividePlayers([3, 3, 6, 9]) == -1


def test_divide_players_empty_list() -> None:
    solution = Solution()
    assert solution.dividePlayers([]) == 0


def test_divide_players_single_pair() -> None:
    solution = Solution()
    assert solution.dividePlayers([1, 1]) == 1
    assert solution.dividePlayers([2, 2]) == 4


def test_divide_players_large_numbers() -> None:
    solution = Solution()
    assert solution.dividePlayers([1000000, 1000000, 1000000, 1000000]) == 2000000000000


if __name__ == "__main__":
    pytest.main()
