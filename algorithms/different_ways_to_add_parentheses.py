from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo: dict[str, List[int]] = {}

        def compute(expression: str) -> List[int]:
            if expression in memo:
                return memo[expression]
            if expression.isdigit():
                memo[expression] = [int(expression)]
                return [int(expression)]
            results = []
            for i, char in enumerate(expression):
                if char in "+-*":
                    left_results = compute(expression[:i])
                    right_results = compute(expression[i + 1 :])
                    for l in left_results:
                        for r in right_results:
                            if char == "+":
                                results.append(l + r)
                            elif char == "-":
                                results.append(l - r)
                            elif char == "*":
                                results.append(l * r)
            memo[expression] = results
            return results

        return compute(expression)
