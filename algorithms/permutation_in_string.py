from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        # Count frequencies of characters in s1
        s1_count = Counter(s1)
        window_count: Counter[str] = Counter()

        # Sliding window over s2, size of window is len(s1)
        for i in range(len(s2)):
            # Add current character to the window count
            window_count[s2[i]] += 1

            # Remove the character that is left behind the window
            if i >= len(s1):
                if window_count[s2[i - len(s1)]] == 1:
                    del window_count[s2[i - len(s1)]]
                else:
                    window_count[s2[i - len(s1)]] -= 1

            # Compare the window with the s1 frequency count
            if window_count == s1_count:
                return True

        return False
