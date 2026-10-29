import heapq as hq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        hq.heapify_max(heap)
        for point in points:
            x = point[0]
            y = point[1]
            res = math.sqrt((x*x) + (y*y))
            print(res)
            if len(heap) < k:
                hq.heappush_max(heap,(res,[x,y]))
            elif res < heap[0][0]:
                hq.heapreplace_max(heap, (res,[x,y]))
        #print(heap)
        return [hq[1] for hq in heap]
