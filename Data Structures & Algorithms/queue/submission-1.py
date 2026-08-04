class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        self.size += 1
        if not self.head or not self.tail: # assuming if head is not present tail is not present
            self.head = new_node
            self.tail = self.head
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
    
    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)
        self.size += 1
        if not self.head or not self.tail:
            self.head = new_node
            self.tail = self.head
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        val = self.tail.val
        self.size -= 1
        if self.size == 0:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        val = self.head.val
        self.size -= 1
        if self.size == 0:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return val