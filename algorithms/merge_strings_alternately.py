class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = max(len(word1), len(word2))
        result = ""

        for i in range(0, n):
            char1 = word1[i] if i < len(word1) else ""
            char2 = word2[i] if i < len(word2) else ""
            result += char1 + char2

        return result
