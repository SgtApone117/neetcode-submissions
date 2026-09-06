class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for ops in s:
            if ops in closeToOpen:  
                if my_stack and my_stack[-1] == closeToOpen[ops]:
                    my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(ops)
        return True if not my_stack else False