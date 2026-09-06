# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(-1)
        temp_node = dummy_node
        while list1 and list2:
            if list1.val <= list2.val:
                temp_node.next = list1
                list1 = list1.next
            else:
                temp_node.next = list2
                list2 = list2.next
            temp_node = temp_node.next
        while list1:
            temp_node.next = list1
            list1 = list1.next
            temp_node = temp_node.next
        while list2:
            temp_node.next = list2
            list2 = list2.next
            temp_node = temp_node.next
        return dummy_node.next