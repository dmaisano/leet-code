class Solution:
    def minimumSteps(self, s: str) -> int:
        steps = 0
        black_count = 0  # Counts the number of '1's seen so far

        for char in s:
            if char == "1":
                black_count += 1
            elif char == "0":
                steps += black_count

        return steps
