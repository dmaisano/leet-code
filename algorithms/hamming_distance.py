class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # XOR the two numbers to get a number where bits are 1 where x and y differ
        xor = x ^ y
        # Count the number of 1s in the binary representation of the XOR result
        distance = bin(xor).count("1")
        return distance
