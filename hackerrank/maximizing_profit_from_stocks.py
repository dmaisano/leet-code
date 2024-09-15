from typing import List, Union


def maxProfit(prices: Union[List[float], List[int]]) -> float:
    # Initialize variables
    min_price = float("inf")  # A large initial value
    max_profit: float = 0.0  # Maximum profit starts at 0

    # Iterate through the list of prices
    for price in prices:
        # Update the minimum price if the current price is lower
        if price < min_price:
            min_price = price
        # Calculate the potential profit
        potential_profit = price - min_price
        # Update the maximum profit if the current potential profit is higher
        if potential_profit > max_profit:
            max_profit = potential_profit

    return max_profit
