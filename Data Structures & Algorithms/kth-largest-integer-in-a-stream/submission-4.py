import heapq as hq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = hq.nlargest(k,nums)
        self.k = k
        hq.heapify(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            hq.heappush(self.heap,val)
        elif val > self.heap[0]:
            hq.heapreplace(self.heap, val)
        # print(self.heap)
        return self.heap[0]
