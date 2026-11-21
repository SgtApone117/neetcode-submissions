class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmp = [0] * 256
        n = len(s)
        left,right = 0,0
        max_len = 0

        while right < n:
            while hmp[ord(s[right])] == 1:
                hmp[ord(s[left])] -= 1
                left += 1
            hmp[ord(s[right])] += 1
            max_len = max(max_len, right-left + 1)
            right += 1
        return max_len