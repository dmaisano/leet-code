class Solution:
    def reverse(self, x: int) -> int:
      if x == 0: return 0

      isNegative = x < 0
      reverseAbs = int(str(abs(x))[::-1])
      reversed = -1 * reverseAbs if isNegative else reverseAbs
      return 0 if (reversed > 2**31 - 1 or reversed < -2**31) else reversed


if __name__ == "__main__":
  soln = Solution()
  print(soln.reverse(123))
  print(soln.reverse(1534236469))
