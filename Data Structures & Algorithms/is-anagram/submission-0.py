class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map = [0]*256
        for i in range(len(s)):
            map[ord(s[i])] += 1
            map[ord(t[i])] -= 1
        return all(x == 0 for x in map)