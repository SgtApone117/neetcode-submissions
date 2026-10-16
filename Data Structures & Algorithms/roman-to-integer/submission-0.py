class Solution:
    def romanToInt(self, s: str) -> int:
        mpp = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        res = 0
        for idx in range(len(s)):
            current_numeral = mpp[s[idx]]
            next_numeral = mpp[s[idx+1]] if idx + 1 < len(s) else 0
            if current_numeral < next_numeral:
                res -= current_numeral
            else:
                res += current_numeral
        return res