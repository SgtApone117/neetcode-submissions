class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ops in s:
            if stack and ops in (')','}',']'):
                if (stack[-1] == '(' and ops == ')') or (stack[-1] == '{' and ops == '}') or (stack[-1] == '[' and ops == ']'):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ops)
        return True if not stack else False