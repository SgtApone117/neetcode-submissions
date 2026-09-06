class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if not stack:
                stack.append(token)
                continue
            if token == "+":
                y = int(stack.pop())
                x = int(stack.pop())
                stack.append(x+y)
            elif token == "-":
                y = int(stack.pop())
                x = int(stack.pop())
                stack.append(x-y)
            elif token == "*":
                y = int(stack.pop())
                x = int(stack.pop())
                stack.append(x*y)
            elif token == "/":
                y = int(stack.pop())
                x = int(stack.pop())
                stack.append(x/y)
            else:
                stack.append(token)
        return int(stack[0])
                