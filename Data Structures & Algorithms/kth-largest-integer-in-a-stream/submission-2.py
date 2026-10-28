class KthLargest:

    def _heapify_down(self, nums, idx):
        n = len(nums)
        smallest_idx = idx
        left_child  = 2*idx+1
        right_child = 2*idx+2

        if left_child < n and nums[left_child] < nums[smallest_idx]:
            smallest_idx = left_child

        if right_child < n and nums[right_child] < nums[smallest_idx]:
            smallest_idx = right_child
        
        if smallest_idx != idx:
            nums[idx],nums[smallest_idx] = nums[smallest_idx],nums[idx]
            self._heapify_down(nums,smallest_idx)
        return

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-1001] * k
        for i in range(k):
            if i < len(nums):
                self.heap[i] = nums[i]
        internal_nodes = (k//2) - 1
        for i in range(internal_nodes, -1,-1):
            self._heapify_down(self.heap, i)
        for i in range(k,len(nums)):
            if nums[i] > self.heap[0]:
                self.heap[0] = nums[i]
                self._heapify_down(self.heap,0)

    def add(self, val: int) -> int:
        if val > self.heap[0]:
            print(val)
            self.heap[0] = val
            self._heapify_down(self.heap,0)
            print(self.heap)
        return self.heap[0]