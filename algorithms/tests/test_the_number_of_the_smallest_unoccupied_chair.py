import pytest

from algorithms.the_number_of_the_smallest_unoccupied_chair import Solution


def test_smallest_chair() -> None:
    solution = Solution()

    times = [[1, 4], [2, 3], [4, 6]]
    targetFriend = 1
    assert solution.smallestChair(times, targetFriend) == 1

    times = [[3, 10], [1, 5], [2, 6]]
    targetFriend = 0
    assert solution.smallestChair(times, targetFriend) == 2

    times = [[1, 4], [2, 3], [4, 6]]
    targetFriend = 0
    assert solution.smallestChair(times, targetFriend) == 0

    times = [[1, 4], [2, 3], [4, 6], [5, 8]]
    targetFriend = 3
    assert solution.smallestChair(times, targetFriend) == 1

    times = [[1, 4], [2, 3], [4, 6], [5, 8], [7, 9]]
    targetFriend = 4
    assert solution.smallestChair(times, targetFriend) == 0


if __name__ == "__main__":
    pytest.main()
