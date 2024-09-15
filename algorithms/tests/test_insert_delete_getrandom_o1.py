from collections import Counter

import pytest

from algorithms.insert_delete_getrandom_o1 import RandomizedSet


class TestRandomizedSet:

    def test_insert(self) -> None:
        randomized_set = RandomizedSet()

        # Test inserting a new element
        assert randomized_set.insert(1) is True

        # Test inserting the same element again
        assert randomized_set.insert(1) is False

        # Test inserting another new element
        assert randomized_set.insert(2) is True

    def test_remove(self) -> None:
        randomized_set = RandomizedSet()

        # Insert some elements
        randomized_set.insert(1)
        randomized_set.insert(2)

        # Test removing an existing element
        assert randomized_set.remove(1) is True

        # Test removing the same element again
        assert randomized_set.remove(1) is False

        # Test removing an element that was never added
        assert randomized_set.remove(3) is False

    def test_get_random(self) -> None:
        randomized_set = RandomizedSet()

        # Insert elements
        randomized_set.insert(1)
        randomized_set.insert(2)
        randomized_set.insert(3)

        # Test if getRandom returns a value that exists in the set
        for _ in range(100):  # Run multiple times to ensure random distribution
            assert randomized_set.getRandom() in [1, 2, 3]

        # Remove an element and check that it is no longer returned
        randomized_set.remove(2)
        for _ in range(100):
            assert randomized_set.getRandom() in [1, 3]

    def test_insert_remove_sequence(self) -> None:
        randomized_set = RandomizedSet()

        # Insert and remove in sequence, checking the state
        assert randomized_set.insert(1) is True
        assert randomized_set.remove(1) is True
        assert randomized_set.insert(2) is True
        assert randomized_set.remove(1) is False
        assert randomized_set.insert(2) is False
        assert randomized_set.getRandom() == 2

    def test_random_distribution(self) -> None:
        randomized_set = RandomizedSet()

        # Insert elements
        randomized_set.insert(1)
        randomized_set.insert(2)
        randomized_set.insert(3)

        # Check distribution over many runs
        results = []
        for _ in range(1000):
            results.append(randomized_set.getRandom())

        count = Counter(results)

        # Test that all elements appear at least once
        assert count[1] > 0
        assert count[2] > 0
        assert count[3] > 0

        # Optionally, you could check that the distribution is roughly uniform
        assert abs(count[1] - count[2]) < 100
        assert abs(count[2] - count[3]) < 100
        assert abs(count[1] - count[3]) < 100


if __name__ == "__main__":
    pytest.main()
