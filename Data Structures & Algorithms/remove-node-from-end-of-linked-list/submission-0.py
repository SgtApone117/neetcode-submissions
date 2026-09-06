# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinelNode = ListNode(-1)
        sentinelNode.next = head
        firstPtr = sentinelNode
        secondPtr = sentinelNode
        for i in range(n):
            firstPtr = firstPtr.next
        while firstPtr.next:
            firstPtr = firstPtr.next
            secondPtr = secondPtr.next
        secondPtr.next = secondPtr.next.next
        return sentinelNode.next