class Solution:
    def __init__(self) -> None:
        self.less_than_20 = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        self.tens = [
            "",
            "Ten",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num: int) -> str:
        if num < 0:
            raise ValueError("Input must be a non-negative integer")

        if num == 0:
            return "Zero"

        res = ""
        for i in range(len(self.thousands)):
            if num % 1000 != 0:
                res = self.helper(num % 1000) + self.thousands[i] + " " + res
            num //= 1000

        return res.strip()

    def helper(self, num: int) -> str:
        if num == 0:
            return ""
        elif num < 20:
            return self.less_than_20[num] + " "
        elif num < 100:
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:
            return self.less_than_20[num // 100] + " Hundred " + self.helper(num % 100)


if __name__ == "__main__":
    soln = Solution()
    res = soln.numberToWords(-120_000)
    print(res)
