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
        mpp = {}
        temp = head

        while temp:
            new_node = Node(temp.val)
            mpp[temp] = new_node
            temp = temp.next
        
        temp = head
        while temp:
            copy_node = mpp[temp]
            copy_node.next = mpp.get(temp.next)
            copy_node.random = mpp.get(temp.random)
            temp = temp.next
        return mpp[head]

        