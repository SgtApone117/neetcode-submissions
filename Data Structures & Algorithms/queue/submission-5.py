class ListNode:
    def __init__(self, val=0,next=None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.front = None
        self.end = None
        self.size = 0

    def isEmpty(self) -> bool:
        return not (self.front and self.end)

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        self.size += 1
        if self.isEmpty():
            self.front = new_node
            self.end = self.front
            return
        new_node.prev = self.end
        self.end.next = new_node
        self.end = new_node

    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)
        self.size += 1
        if self.isEmpty():
            self.front = new_node
            self.end = self.front
            return
        new_node.next = self.front
        self.front.prev = new_node
        self.front = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        if self.size == 1:
            self.size -= 1
            curr_node = self.end
            val = curr_node.val
            del curr_node
            self.front = self.end = None
            return val
        self.size -= 1
        curr_node = self.end
        val = curr_node.val
        self.end = self.end.prev
        self.end.next = None
        del curr_node
        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        if self.size == 1:
            self.size -= 1
            curr_node = self.end
            val = curr_node.val
            del curr_node
            self.front = self.end = None
            return val
        self.size -= 1
        curr_node = self.front
        val = curr_node.val
        self.front = self.front.next
        self.front.prev = None
        del curr_node
        return val