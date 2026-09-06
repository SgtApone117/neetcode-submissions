class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        for ops in s:
            if ops in ("(","[","{"):
                my_stack.append(ops)
            elif ops in (")","]","}"):
                if len(my_stack) == 0:
                    return False
                get_top = my_stack[-1]
                if (get_top == "(" and ops ==")") or (get_top == "[" and ops == "]") or (get_top == "{" and ops =="}"):
                    my_stack.pop()
                else:
                    return False
            else:
                return False
        if len(my_stack) > 0:
            return False
        return True