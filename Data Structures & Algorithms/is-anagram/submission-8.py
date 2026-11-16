from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = Counter(s)
        count_t = Counter(t)
        # print(count)
        for i in range(len(s)):
            if s[i] in count_t:
                count_t[s[i]] -= 1
            if t[i] in count_s:
                count_s[t[i]] -= 1
        
        for key,value in count_s.items():
            if value != 0:
                return False
        for key,value in count_t.items():
            if value != 0:
                return False
        return True
        