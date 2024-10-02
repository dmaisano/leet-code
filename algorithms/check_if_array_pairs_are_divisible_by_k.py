from collections import defaultdict
from typing import DefaultDict, List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder_count: DefaultDict[int, int] = defaultdict(int)

        # Count the remainders when each element is divided by k
        for num in arr:
            remainder = num % k
            if remainder < 0:
                remainder += k  # Ensure positive remainder
            remainder_count[remainder] += 1

        # Check if valid pairs can be formed
        for remainder in remainder_count:
            # If remainder is 0, we need an even number of such elements
            if remainder == 0:
                if remainder_count[remainder] % 2 != 0:
                    return False
            # If remainder is exactly k/2 (when k is even), we also need an even number of such elements
            elif remainder == k - remainder:
                if remainder_count[remainder] % 2 != 0:
                    return False
            else:
                # The count of elements with remainder r should be equal to the count of elements with remainder k - r
                if remainder_count[remainder] != remainder_count[k - remainder]:
                    return False

        return True
