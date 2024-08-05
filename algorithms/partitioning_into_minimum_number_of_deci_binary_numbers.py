class Solution:
    def minPartitions(self, n: str) -> int:
        max_digit = max(map(int, n))
        return max_digit


if __name__ == "__main__":
    res = Solution().min_deci_binary_numbers("27346209830709182346")
    print(res)
