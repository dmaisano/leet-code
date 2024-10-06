class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()

        if len(words1) < len(words2):
            words1, words2 = words2, words1

        # Two pointers for checking matching words from both sides
        i, j = 0, 0

        # Check matching from the start
        while i < len(words2) and words1[i] == words2[i]:
            i += 1

        # Check matching from the end
        while j < len(words2) and words1[-(j + 1)] == words2[-(j + 1)]:
            j += 1

        # The sentences are similar if the sum of i and j is at least the length of words2
        return i + j >= len(words2)
