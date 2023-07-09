class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        shift = 31
        while n: 
            if n & 1: 
                 # Put the 1 in the shift slot (from the right).
                reverse = reverse | (1 << shift)
            shift -= 1
            n = n >> 1
        return reverse
        
