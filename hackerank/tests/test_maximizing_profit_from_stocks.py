import pytest

from ..maximizing_profit_from_stocks import maxProfit


def test_maxProfit() -> None:
    # Test cases
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5.0),  # Buy at 1, sell at 6 for a profit of 5
        ([7, 6, 4, 3, 1], 0.0),  # No profit can be made
        ([1, 2, 3, 4, 5], 4.0),  # Buy at 1, sell at 5 for a profit of 4
        ([3, 3, 3, 3], 0.0),  # All prices are the same, no profit
        ([2, 4, 1, 5], 4.0),  # Buy at 1, sell at 5 for a profit of 4
    ]

    for prices, expected in test_cases:
        assert maxProfit(prices) == expected


if __name__ == "__main__":
    pytest.main()
