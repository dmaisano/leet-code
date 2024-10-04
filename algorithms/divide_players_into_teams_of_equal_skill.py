from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if not skill:
            return 0

        skill.sort()
        n = len(skill)
        target_sum = skill[0] + skill[-1]
        total_chemistry = 0

        for i in range(n // 2):
            if skill[i] + skill[n - i - 1] != target_sum:
                return -1
            total_chemistry += skill[i] * skill[n - i - 1]

        return total_chemistry
