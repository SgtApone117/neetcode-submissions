class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m:
            return False
        freq_count = [0] * 26

        for ch in s:
            freq_count[ord(ch) - 97] += 1
        for ch in t:
            if freq_count[ord(ch) - 97] > 0:
                freq_count[ord(ch) - 97] -= 1
            else:
                return False
        return True
            

        