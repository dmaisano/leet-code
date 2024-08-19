class Solution:
    def findComplement(self, num: int) -> int:
        # Find the number of bits in num
        num_bits = num.bit_length()
        # Create a mask with all bits set to 1 that is the same length as num
        mask = (1 << num_bits) - 1
        # XOR num with the mask to flip all bits
        return num ^ mask
