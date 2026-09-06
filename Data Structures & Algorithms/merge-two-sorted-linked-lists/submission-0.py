# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        currNode = dummyNode
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                currNode.next = l1
                l1 = l1.next
            else:
                currNode.next = l2
                l2 = l2.next
            currNode = currNode.next
        while l1 != None:
            currNode.next = l1
            l1 = l1.next
            currNode = currNode.next
        while l2 != None:
            currNode.next = l2
            l2 = l2.next
            currNode = currNode.next
        return dummyNode.next