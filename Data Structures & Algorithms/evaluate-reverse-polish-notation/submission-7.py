class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ('+','-','*','/'):
                operand_1 = stack.pop()
                operand_2 = stack.pop()
                if token == "+":
                    res = operand_1 + operand_2
                    stack.append(res)
                elif token == "-":
                    res = operand_2-operand_1
                    stack.append(res)
                elif token == "*":
                    res = operand_1 * operand_2
                    stack.append(res)
                elif token == "/":
                    res = operand_2 / operand_1
                    stack.append(int(res))
            else:
                stack.append(int(token))
        return stack[-1]
