from collections import Counter,deque
import heapq as hq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        # simulate maxheap by marking the count as negative
        heap = [-cnt for cnt in count.values()]

        hq.heapify(heap)
        q = deque()
        time = 0

        while heap or q:
            time += 1
            if heap:
                cnt = hq.heappop(heap)
                cnt += 1 # they are negative hence add to simulate 

                if cnt < 0:
                    # queue (task freq and time to wait)
                    q.append([cnt, time+n])
            
            if q and q[0][1] == time:
                hq.heappush(heap,q.popleft()[0])
        return time
            

