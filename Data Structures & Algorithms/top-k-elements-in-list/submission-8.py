from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mpp = defaultdict(int)
        for num in nums:
            mpp[num] += 1
        val_key_mpp = defaultdict(list)

        for key,val in mpp.items():
            val_key_mpp[val].append(key)
        # print(val_key_mpp)
        res = []
        count = 0
        for i in range(len(nums), 0, -1):
            if count == k:
                break
            if val_key_mpp[i]:
                for val in val_key_mpp[i]:
                    if count == k:
                        break
                    res.append(val)
                    count += 1
        return res

        