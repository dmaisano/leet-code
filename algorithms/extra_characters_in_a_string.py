from typing import List
from sys import maxsize


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [maxsize] * (n + 1)
        dp[0] = 0

        dictionary_set = set(dictionary)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1

            for j in range(i):
                if s[j:i] in dictionary_set:
                    dp[i] = min(dp[i], dp[j])

        return dp[n]
