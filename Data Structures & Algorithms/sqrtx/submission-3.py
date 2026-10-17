class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        res = 0
        while i * i <= x:
            res = i
            i += 1
        return res