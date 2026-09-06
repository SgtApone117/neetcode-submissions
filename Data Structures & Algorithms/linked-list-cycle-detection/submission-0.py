# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowNode = head
        fastNode = head.next
        while slowNode != fastNode:
            if fastNode == None or fastNode.next == None:
                return False
            slowNode = slowNode.next
            fastNode = fastNode.next.next
        return True
        