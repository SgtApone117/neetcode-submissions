class Solution:
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647
        if x >= MAX or x <= MIN or x == 0:
            return 0
        res = 0
        neg = False
        if x < 0:
            neg = True
        x = abs(x)
        total_digit = int(math.log10(x))
        mul_number = 10**total_digit
        while x:
            digit = x % 10
            if mul_number >= 1:
                res += digit * mul_number
                mul_number //= 10
            x //= 10
        if neg:
            res = -res
        return res if res < MAX and res > MIN else 0