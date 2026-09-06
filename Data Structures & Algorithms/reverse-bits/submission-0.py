class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            ith_bit = (n >> i) & 1
            if ith_bit == 1:
                res |= (1 << (31 - i))
        return res
