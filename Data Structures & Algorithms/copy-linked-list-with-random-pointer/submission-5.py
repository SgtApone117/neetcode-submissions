"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        # weave
        temp = head
        while temp:
            new_node = Node(temp.val)
            next_node = temp.next
            new_node.next = next_node
            temp.next = new_node
            temp = temp.next.next
        
        # wire
        temp = head
        while temp:
            if temp.random:
                temp.next.random = temp.random.next
            temp = temp.next.next
        
        # Un-weave
        temp = head
        copy_head = head.next
        while temp:
            copy_node = temp.next
            temp.next = copy_node.next
            temp = temp.next
            if temp:
                copy_node.next = temp.next
        return copy_head