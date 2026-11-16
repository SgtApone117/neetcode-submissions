import heapq as hq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        heap = []
        # print(count)
        for key,value in count.items():
            if len(heap) < k:
                hq.heappush(heap, (value,key))
            elif heap and len(heap) == k and heap[0][0] < value:
                hq.heappop(heap)
                hq.heappush(heap, (value,key))
        # print(heap)
        return list(val[1] for val in heap)
        