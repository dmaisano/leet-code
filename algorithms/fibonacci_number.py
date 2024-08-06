class Solution:
    cache: dict[int, int] = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        if n < 0:
            raise ValueError("n must be a non-negative integer")

        if n in self.cache:
            return self.cache[n]

        self.cache[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.cache[n]
