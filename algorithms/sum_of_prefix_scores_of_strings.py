from typing import Dict


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, "TrieNode"] = {}
        self.count = 0


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1

    def getPrefixScore(self, word: str) -> int:
        node = self.root
        score = 0
        for char in word:
            if char in node.children:
                node = node.children[char]
                score += node.count
            else:
                break
        return score


class Solution:
    def sumPrefixScores(self, words: list[str]) -> list[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        return [trie.getPrefixScore(word) for word in words]
