# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        my_list = []
        temp = head

        while temp:
            my_list.append(temp.val)
            temp = temp.next

        n = len(my_list)
        for i in range(0,n,k):
            if i + k <= n:
                my_list[i:i+k] = reversed(my_list[i:i+k])
        
        dummy_node = ListNode(-1)
        temp = dummy_node

        for num in my_list:
            temp.next = ListNode(num)
            temp = temp.next
        return dummy_node.next