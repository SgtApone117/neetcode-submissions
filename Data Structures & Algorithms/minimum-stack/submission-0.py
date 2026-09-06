class MinStack:

    def __init__(self):
        self.my_stack = []

    def push(self, val: int) -> None:
        if self.my_stack:
            get_min_till_now = self.my_stack[-1][1]
            self.my_stack.append((val, min(get_min_till_now, val)))
        else:
            self.my_stack.append((val,val))

    def pop(self) -> None:
        self.my_stack.pop()

    def top(self) -> int:
        return self.my_stack[-1][0]

    def getMin(self) -> int:
        return self.my_stack[-1][1]
        
