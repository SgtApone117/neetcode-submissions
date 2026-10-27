class MinHeap:
    
    def __init__(self):
        self.heap = []
        self.size = 0
    def _heapify_up(self, nums, idx):
        parent_idx = (idx-1)//2
        if idx > 0 and nums[idx] < nums[parent_idx]:
            nums[idx],nums[parent_idx] = nums[parent_idx],nums[idx]
            self._heapify_up(nums,parent_idx)
        return
    
    def _heapify_down(self, nums, idx):
        smallest_idx = idx
        left_child = 2*idx + 1
        right_child = 2*idx + 2
        n = len(nums)

        if left_child < n and nums[left_child] < nums[smallest_idx]:
            smallest_idx = left_child
        
        if right_child < n and nums[right_child] < nums[smallest_idx]:
            smallest_idx = right_child
        
        if smallest_idx != idx:
            nums[idx],nums[smallest_idx] = nums[smallest_idx],nums[idx]
            self._heapify_down(nums, smallest_idx)
        return

    def push(self, val: int) -> None:
        self.heap.append(val)
        self._heapify_up(self.heap, self.size)
        self.size += 1
        return

    def pop(self) -> int:
        if self.size == 0:
            return -1
        element = self.heap[0]
        self.heap[0],self.heap[self.size - 1] = self.heap[self.size - 1], self.heap[0]
        self.heap.pop()
        self.size -= 1
        
        if self.size > 0:
            self._heapify_down(self.heap, 0)
        return element

    def top(self) -> int:
        return self.heap[0] if self.size > 0 else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = nums
        n = len(nums)
        self.size = n
        internal_nodes = (n//2)-1

        for node in range(internal_nodes, -1, -1):
            self._heapify_down(self.heap, node)
        