from typing import List


class CustomStack:
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack: List[int] = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop() if self.stack else -1

    def increment(self, k: int, val: int) -> None:
        limit = min(k, len(self.stack))
        for i in range(limit):
            self.stack[i] += val
