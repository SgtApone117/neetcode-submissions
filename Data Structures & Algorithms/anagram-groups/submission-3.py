from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmp = {}
        for word in strs:
            count = Counter(word)
            # print(count)
            key = ""
            for i in range(26):
                key += (chr(i+97)+str(count[chr(i+97)]))
            # print(key)
            if key not in hmp:
                hmp[key] = []
            hmp[key].append(word)
        return list(hmp.values())