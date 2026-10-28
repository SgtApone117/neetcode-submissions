class Solution:
    def _heapify_down(self, nums, idx):
        smallest_idx = idx
        n = len(nums)
        left_child  = 2*idx+1
        right_child = 2*idx+2

        if left_child < n and nums[left_child] < nums[smallest_idx]:
            smallest_idx = left_child
        if right_child < n and nums[right_child] < nums[smallest_idx]:
            smallest_idx = right_child
        
        if smallest_idx != idx:
            nums[idx],nums[smallest_idx] = nums[smallest_idx],nums[idx]
            self._heapify_down(nums,smallest_idx)
    

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = [0] * k

        for i in range(k):
            heap[i] = nums[i]
        
        internal_nodes = (k//2)-1
        for node_idx in range(internal_nodes,-1,-1):
            self._heapify_down(heap, node_idx)
        for i in range(k,n):
            if heap[0] < nums[i]:
                heap[0] = nums[i]
                self._heapify_down(heap,0)
        return heap[0]
        
