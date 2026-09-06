class Solution:
    def calPoints(self, operations: List[str]) -> int:
        my_stack = []
        for op in operations:
            if op == "+":
                x,y = my_stack.pop(),my_stack.pop()
                my_stack.append(y)
                my_stack.append(x)
                my_stack.append(int(x+y))
            elif op == "C":
                removed_element = my_stack.pop()
            elif op == "D":
                x = my_stack.pop()
                my_stack.append(x)
                my_stack.append(x*2)
            else:
                my_stack.append(int(op))
            print(my_stack)
        return sum(my_stack) 
