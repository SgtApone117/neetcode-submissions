class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmp = {}
        for word in strs:
            ch_map = [0] * 26
            for ch in word:
                ch_map[ord(ch)-97] += 1
            key = ""
            for i in range(26):
                key += chr(i+97) + str(ch_map[i])
                #print(key)
            if key not in hmp:
                hmp[key] = []
            hmp[key].append(word)
        return list(hmp.values())
