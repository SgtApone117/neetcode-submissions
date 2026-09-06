class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for token in tokens:
            if token == "+":
                x, y = stack.pop(), stack.pop()
                stack.append(x+y)
            elif token == "-":
                x, y = stack.pop(), stack.pop()
                stack.append(y-x)
            elif token == "*":
                x, y = stack.pop(), stack.pop()
                stack.append(x*y)
            elif token == "/":
                x, y = stack.pop(), stack.pop()
                stack.append(int(y/x))
            else:
                stack.append(int(token))
        return stack[-1]
        
        