# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasKNodes(self, head, k):
        count = 0
        while head and count < k:
            head = head.next
            count += 1
        return k == count
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # check if have k nodes
        if(not self.hasKNodes(head, k)):
            return head
        prev = None
        curr = head
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
         
        head.next = self.reverseKGroup(curr,k)
        return prev

