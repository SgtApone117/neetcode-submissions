import heapq as hq
class MedianFinder:
    def __init__(self):
        self.smaller_half = [] # max_heap
        self.taller_half = [] # min_heap

    def addNum(self, num: int) -> None:
        hq.heappush(self.smaller_half, -num)

        # ensure smaller half largest is smaller than taller halfs smallest
        if self.smaller_half and self.taller_half and (-self.smaller_half[0] > self.taller_half[0]):
            val = -hq.heappop(self.smaller_half)
            hq.heappush(self.taller_half, val)
        
        # balance the sizes (keep smaller half one larger)
        if len(self.smaller_half) > len(self.taller_half) + 1:
            val = -hq.heappop(self.smaller_half)
            hq.heappush(self.taller_half, val)
        elif len(self.taller_half) > len(self.smaller_half):
            val = hq.heappop(self.taller_half)
            hq.heappush(self.smaller_half, -val)

    def findMedian(self) -> float:
        if len(self.smaller_half) > len(self.taller_half):
            return -self.smaller_half[0]
        else:
            return (-self.smaller_half[0] + self.taller_half[0])/2.0        
        