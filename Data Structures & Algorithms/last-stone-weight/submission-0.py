class Solution:
    def _heapify_down(self, nums, idx):
        n = len(nums)
        largest_idx = idx
        left_child  = 2*idx+1
        right_child = 2*idx+2

        if left_child < n and nums[left_child] > nums[largest_idx]:
            largest_idx = left_child
        if right_child < n and nums[right_child] > nums[largest_idx]:
            largest_idx = right_child
        
        if largest_idx != idx:
            nums[idx],nums[largest_idx] = nums[largest_idx],nums[idx]
            self._heapify_down(nums, largest_idx)

    def _heapify_up(self,nums,idx):
        parent_idx = (idx-1)//2
        if idx > 0 and nums[idx] > nums[parent_idx]:
            nums[idx],nums[parent_idx] = nums[parent_idx],nums[idx]
            self._heapify_up(nums,parent_idx)
        
    
    def ExtractMax(self, nums,n):
        element = nums[0]
        nums[0],nums[n-1] = nums[n-1],nums[0]
        nums.pop()
        self._heapify_down(nums,0)
        return element
    
    def Insert(self,nums,val):
        nums.append(val)
        self._heapify_up(nums, len(nums)-1)

    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        # heap = [0] * n
        internal_nodes = (n//2)-1
        for i in range(internal_nodes,-1,-1):
            self._heapify_down(stones, i)
        print(stones)
        while len(stones) > 1:
            y = self.ExtractMax(stones, len(stones))
            print(y)
            x = self.ExtractMax(stones, len(stones))
            print(x)
            print(stones)
            if y > x:
                self.Insert(stones,y-x)
        print(stones)
        return stones[0] if len(stones) == 1 else 0
        