from typing import List


class Solution:
    row1 = set("qwertyuiop")
    row2 = set("asdfghjkl")
    row3 = set("zxcvbnm")

    def findWords(self, words: List[str]) -> List[str]:
        result = []

        for word in words:
            lower_word = word.lower()
            if (
                set(lower_word).issubset(self.row1)
                or set(lower_word).issubset(self.row2)
                or set(lower_word).issubset(self.row3)
            ):
                result.append(word)

        return result
