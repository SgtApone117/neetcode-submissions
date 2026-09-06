class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val,val))
        else:
            last_stack_value = self.stack[-1]
            if last_stack_value != -1:
                min_val = min(val, last_stack_value[1])
                self.stack.append((val,min_val))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return -1
        

    def getMin(self) -> int:
        if self.stack:
            get_top = self.stack[-1]
            if get_top != -1:
                return get_top[1]
        return -1
        
