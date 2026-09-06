# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slowNode = fastNode = head
        while fastNode and fastNode.next:
            slowNode = slowNode.next
            fastNode = fastNode.next.next
        secondListHead = slowNode.next
        slowNode.next = None
        prev = None
        while secondListHead:
            tempNode = secondListHead.next
            secondListHead.next = prev
            prev = secondListHead
            secondListHead = tempNode
        secondListHead = prev
        currNode = head
        while secondListHead:
            tempNode1, tempNode2 = secondListHead.next, currNode.next
            secondListHead.next = currNode.next
            currNode.next = secondListHead
            secondListHead,currNode = tempNode1, tempNode2
        

        

        