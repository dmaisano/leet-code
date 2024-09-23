class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # Helper function to count steps between two numbers within the range of [1, n]
        def count_steps(prefix: int, n: int) -> int:
            current = prefix
            next_prefix = prefix + 1
            steps = 0
            while current <= n:
                steps += min(n + 1, next_prefix) - current
                current *= 10
                next_prefix *= 10
            return steps

        current = 1
        k -= 1  # We start from the first number, so reduce k by 1

        while k > 0:
            steps = count_steps(current, n)
            if (
                steps <= k
            ):  # Move to the next prefix if there are not enough steps in the current range
                k -= steps
                current += 1  # Move to the next lexicographical number
            else:  # Dive into the current prefix
                k -= 1
                current *= 10  # Go to the next level in the tree (e.g., from 1 -> 10)

        return current
