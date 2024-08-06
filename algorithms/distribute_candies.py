from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_candies = len(set(candyType))  # 5
        max_allowed_candies = len(candyType) // 2  # 6
        return min(unique_candies, max_allowed_candies)
