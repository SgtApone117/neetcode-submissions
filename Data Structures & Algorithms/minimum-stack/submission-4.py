class MinStack:

    def __init__(self):
        self.main_stack = []

    def push(self, val: int) -> None:
        if not self.main_stack:
            self.main_stack.append((val, val))
        else:
            top_val, min_val = self.main_stack[-1]
            self.main_stack.append((val, min(min_val,val)))

    def pop(self) -> None:
        if self.main_stack:
            self.main_stack.pop()

    def top(self) -> int:
        if self.main_stack:
            top_val, min_val = self.main_stack[-1]
            return top_val

    def getMin(self) -> int:
        if self.main_stack:
            top_val, min_val = self.main_stack[-1]
            return min_val
        
