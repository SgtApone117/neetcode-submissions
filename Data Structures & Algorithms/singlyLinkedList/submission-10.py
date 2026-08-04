class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        for _ in range(index):
            if not curr:
                return -1
            curr = curr.next
        if curr:
            return curr.val
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr and curr.next:
            curr = curr.next
        curr.next = new_node

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        curr = self.head
        for _ in range(index-1):
            if not curr or not curr.next:
                return False
            curr = curr.next
        if not curr or not curr.next:
            return False
        if curr.next:
            new_node = curr.next
            curr.next = new_node.next
            del new_node
        else:
            del curr
        return True

    def getValues(self) -> List[int]:
        result = []
        curr = self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result
        
