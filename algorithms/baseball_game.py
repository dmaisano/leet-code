from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record: List[int] = []

        for op in operations:
            match op:
                case "C":
                    record.pop()
                case "D":
                    record.append(2 * record[-1])
                case "+":
                    record.append(record[-1] + record[-2])
                case _:
                    record.append(int(op))

        return sum(record)
