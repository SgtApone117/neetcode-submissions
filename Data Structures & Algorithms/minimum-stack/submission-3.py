class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if self.min_stack:
            x = min(val, self.min_stack[-1])
        else:
            x = val
        self.min_stack.append(x)

    def pop(self) -> None:
        if self.main_stack:
            self.main_stack.pop()
        if self.min_stack:
            self.min_stack.pop()

    def top(self) -> int:
        if self.main_stack:
            return self.main_stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        
