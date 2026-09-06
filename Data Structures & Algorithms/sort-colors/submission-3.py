class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def Insert(self, head, val):
        new_node = ListNode(val)
        new_node.next = head
        return new_node
    
    def Delete(self,head):
        if not head:
            return None, None
        val = head.val
        new_head = head.next
        return val, new_head

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [None] * 3

        for num in nums:
            buckets[num] = self.Insert(buckets[num], num)
        
        idx = 0
        for color in range(3):
            head = buckets[color]
            while head:
                val , head = self.Delete(head)
                nums[idx] = val
                idx += 1

        