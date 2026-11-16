import heapq as hq
from collections import Counter,defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        val_key_mpp = defaultdict(list)

        for key,val in count.items():
            val_key_mpp[val].append(key)
        count = 0
        res = []
        for i in range(len(nums),-1,-1):
            if count == k:
                break
            if val_key_mpp[i]:
                for val in val_key_mpp[i]:
                    if count == k:
                        break
                    res.append(val)
                    count += 1
        return res
        