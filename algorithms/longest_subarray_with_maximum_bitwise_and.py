from typing import List


class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        """
        1. Identify the maximum value in the array
        2. The bitwise AND of multiple numbers will always be less than or equal to the largest number in the array
        3. Look for the longest contiguous subarray where all elements are equal to this maximum value
        """
        # Find the maximum value in the array
        max_value = max(nums)

        # Initialize variables to track the longest subarray length
        longest = 0
        current_length = 0

        # Iterate through the array
        for num in nums:
            if num == max_value:
                # If the current number is equal to max_value, increment the length of the current subarray
                current_length += 1
                longest = max(longest, current_length)
            else:
                # Reset the current length if the number is not equal to max_value
                current_length = 0

        return longest
