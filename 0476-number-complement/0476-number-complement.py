class Solution:
    def findComplement(self, num: int) -> int:
        # Calculate the bit length of num
        bit_length = num.bit_length()
        
        # Create a bitmask with all bits set to 1, having the same length as num's binary representation
        bitmask = (1 << bit_length) - 1
        
        # XOR num with the bitmask to get the complement
        return num ^ bitmask