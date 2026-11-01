class Solution:
    def HelperFunction(self, n):
        res = 0
        while n > 0:
            rem = n % 10
            res += (rem * rem) if rem != 0 else 0
            n //= 10
        return res

    def isHappy(self, n: int) -> bool:
        st = set()
        while n != 1:
            if n in st:
                return False
            st.add(n)
            # print(n)
            n = self.HelperFunction(n)
        return True
