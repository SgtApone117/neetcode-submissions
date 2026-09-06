from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        n = len(self.q)
        self.q.append(x)

        for _ in range(n):
            element = self.q.popleft()
            self.q.append(element)

    def pop(self) -> int:
        element = self.q.popleft()
        return element

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        n = len(self.q)
        return (n == 0)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()