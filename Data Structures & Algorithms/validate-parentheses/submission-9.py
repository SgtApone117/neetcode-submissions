class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        for p in s:
            if p in ['[','(','{']:
                my_stack.append(p)
            else:
                if my_stack:
                    top = my_stack[-1]
                    if (top == '[' and p == ']') \
                        or (top == '(' and p == ')') \
                        or (top == '{' and p == '}'):
                            my_stack.pop()
                    else:
                        return False
                else:
                    return False
        print(my_stack)
        return True if len(my_stack) == 0 else False