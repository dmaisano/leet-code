from typing import List

import pytest

from ..stock_max.stock_max import stockmax


def test_stockmax() -> None:
    # Test case 1: Empty list
    prices: List[int] = []
    assert stockmax(prices) == 0

    # Test case 2: Single price
    prices = [10]
    assert stockmax(prices) == 0

    # Test case 3: Increasing prices
    prices = [1, 2, 3, 4, 5]
    assert stockmax(prices) == 10

    # Test case 4: Decreasing prices
    prices = [5, 4, 3, 2, 1]
    assert stockmax(prices) == 0

    # Test case 5: Random prices
    prices = [7, 1, 5, 3, 6, 4]
    assert stockmax(prices) == 9

    # Test case 6: Random prices with negative values
    prices = [7, -1, 5, 3, 6, 4]
    assert stockmax(prices) == 11

    # Test case 7: Random prices with duplicate values
    prices = [7, 1, 5, 3, 6, 4, 5, 5]
    assert stockmax(prices) == 10

    # Test case 8: Large prices
    prices = [1000000] * 100000
    assert stockmax(prices) == 0

    # Test case 9: Large prices with one maximum value
    prices = [1] * 99999 + [1000000]
    assert stockmax(prices) == 99_998_900_001

    # Test case 10: Large prices with multiple maximum values
    prices = [1] * 99999 + [1000000, 1000000]
    assert stockmax(prices) == 99_998_900_001


if __name__ == "__main__":
    pytest.main()
