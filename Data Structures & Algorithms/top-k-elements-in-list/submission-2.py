class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        max_val = max(count.values())
        freq_list = [[] for _ in range(max_val + 1)]
        for key,value in count.items():
            freq_list[value].append(key)
        res = []
        count = 0
        for i in range(len(freq_list)-1,-1,-1):
            if count == k:
                break
            if freq_list[i]:
                for num in freq_list[i]:
                    res.append(num)
                    count += 1
        return res