import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heap = []
        print(stones)
        hq.heapify_max(stones)
        print(stones)
        while len(stones) > 1:
            y = hq.heappop_max(stones)
            x = hq.heappop_max(stones)
            if y > x:
                hq.heappush_max(stones,y-x)
        
        return stones[0] if len(stones) == 1 else 0