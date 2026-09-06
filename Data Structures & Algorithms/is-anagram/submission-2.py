class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m:
            return False
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        for i in range(n):
            if sorted_s[i] != sorted_t[i]:
                return False
        return True
        