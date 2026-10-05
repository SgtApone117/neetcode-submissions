class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmpp = [0] * 26
        for ch in s:
            hmpp[ord(ch) - 97] += 1
        # print(hmpp)
        for ch in t:
            if hmpp[ord(ch)-97] > 0:
                hmpp[ord(ch)-97] -= 1
            else:
                return False
        return True