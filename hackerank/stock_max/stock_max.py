def stockmax(prices: list[int]) -> int:
    n = len(prices)
    max_profit = 0
    max_price = 0

    if n == 0:
        return 0

    for i in range(n - 1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]

        max_profit += max_price - prices[i]

    return max_profit
