class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 0
        val = -1
        for i in range(len(digits)-1,-1,-1):
            if i == len(digits) - 1:
                val = digits[i] + 1
                carry = val // 10
                val = val % 10
            else:
                val = digits[i] + carry
                carry = val // 10
                val = val % 10
            res.append(val)
        if carry == 1:
            res.append(1)
        return res[::-1]