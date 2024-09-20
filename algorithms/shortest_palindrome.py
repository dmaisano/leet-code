class Solution:
    def shortestPalindrome(self, s: str) -> str:
        """
        https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
        """
        reverse_s = s[::-1]

        new_s = s + "#" + reverse_s  # the '#' is a separator

        n = len(new_s)  # Create the KMP table (partial match table)
        longest_prefix_suffix = [
            0
        ] * n  # LPS array to hold the longest prefix wich is also suffix lengths

        # Build the KMP table for the new string
        for i in range(1, n):
            j = longest_prefix_suffix[i - 1]

            while j > 0 and new_s[i] != new_s[j]:
                j = longest_prefix_suffix[j - 1]

            if new_s[i] == new_s[j]:
                j += 1

            longest_prefix_suffix[i] = j

        # The last value of lps will give us the longest palindromic prefix
        longest_palindromic_prefix_length = longest_prefix_suffix[-1]

        # Add the remaining characters from rev_s to the front of the original string
        return reverse_s[: len(s) - longest_palindromic_prefix_length] + s
