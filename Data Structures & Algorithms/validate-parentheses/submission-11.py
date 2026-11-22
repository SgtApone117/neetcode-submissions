class Solution:
    def isValid(self, s: str) -> bool:
        hmp_dict = {')':'(','}':'{',']':'['}
        stack = []
        n = len(s)

        for i in range(n):
            if s[i] in hmp_dict:
                if stack and stack[-1] == hmp_dict[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        return True if not stack else False


            