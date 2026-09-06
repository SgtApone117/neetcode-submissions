class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = dict()
        result = []
        for word in strs:
            wordFreq = [0] * 26
            for ch in word:
                wordFreq[ord(ch)-97] += 1
            key = ""
            for i in range(26):
                key += chr(i+97) + chr(wordFreq[i])
            if key not in map:
                map[key] = []
            map[key].append(word)
        return list(map.values())
