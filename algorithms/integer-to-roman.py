from pprint import pprint

class Solution:
    def intToRoman(self, num: int) -> str:
      val = [
          1000, 900, 500, 400,
          100, 90, 50, 40,
          10, 9, 5, 4, 1
      ]
      syms = [
          "M", "CM", "D", "CD",
          "C", "XC", "L", "XL",
          "X", "IX", "V", "IV",
          "I"
      ]
      roman_num = ''
      i = 0
      while num > 0:
          for _ in range(num // val[i]):
              roman_num += syms[i]
              num -= val[i]
          i += 1
      return roman_num


if __name__ == "__main__":
    soln = Solution()
    res = soln.intToRoman(58)
    pprint(res)
