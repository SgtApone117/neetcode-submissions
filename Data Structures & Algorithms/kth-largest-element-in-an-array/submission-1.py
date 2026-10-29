import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        hq.heapify(heap)

        for num in nums:
            if len(heap) < k:
                hq.heappush(heap,num)
            elif num > heap[0]:
                hq.heapreplace(heap,num)
        return heap[0]