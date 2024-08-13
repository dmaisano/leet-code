from dataclasses import dataclass
from random import choice as random_choice
from typing import Any, Dict, List


@dataclass
class RandomizedSet:
    data: List[int]
    index_map: Dict[int, int]

    def __init__(self) -> None:
        self.data = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.data.append(val)
        self.index_map[val] = len(self.data) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        last_element = self.data[-1]
        idx_to_remove = self.index_map[val]

        # Move the last element to the position of the element to be removed
        self.data[idx_to_remove] = last_element
        self.index_map[last_element] = idx_to_remove

        # Remove the last element
        self.data.pop()
        del self.index_map[val]

        return True

    def getRandom(self) -> int:
        return random_choice(self.data)
