class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        if not arr:
            return []

        sorted_unique = sorted(set(arr))
        rank_map = {num: rank + 1 for rank, num in enumerate(sorted_unique)}
        return [rank_map[num] for num in arr]
