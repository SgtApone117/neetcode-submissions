# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sentinelNode = ListNode(-1)
        res = sentinelNode
        carry = 0
        while l1 != None or l2 != None or carry == 1:
            sum = (l1.val if l1 != None else 0) + (l2.val if l2 != None else 0) + carry
            carry = sum//10
            newNode = ListNode(sum%10)
            res.next = newNode
            res = res.next
            l1 = l1.next if l1 != None else None
            l2 = None if l2 == None else l2.next
        return sentinelNode.next