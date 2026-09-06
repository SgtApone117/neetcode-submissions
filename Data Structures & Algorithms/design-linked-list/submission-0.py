class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

class MyLinkedList:

    def __init__(self):
        self.my_list = ListNode()

    def get(self, index: int) -> int:
        curr_node = self.my_list
        for _ in range(index):
            if not curr_node.next:
                return -1
            curr_node = curr_node.next
        if curr_node.next:
            return curr_node.next.val
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.my_list.next
        self.my_list.next = new_node

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        curr_head = self.my_list
        while curr_head.next:
            curr_head = curr_head.next
        curr_head.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        curr_node = self.my_list
        for _ in range(index):
            if not curr_node.next:
                return
            curr_node = curr_node.next
        new_node = ListNode(val)
        new_node.next = curr_node.next
        curr_node.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        curr_node = self.my_list
        for _ in range(index):
            if not curr_node.next:
                return
            curr_node = curr_node.next
        if curr_node.next:
            curr_node.next = curr_node.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)