from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmp = defaultdict(int)
        for num in nums:
            hmp[num] += 1
        res = []
        # print(hmp)
        st = set()
        max_key = float('-inf')
        max_occurrence = float('-inf')
        for key,val in hmp.items():
            if val > max_occurrence:
                max_occurrence = val
                max_key = key
        st.add(max_key)
        res.append(max_key)
        k -= 1
        
        while k > 0:
            max_key = float('-inf')
            max_occurrence = float('-inf')
            for key,val in hmp.items():
                if key not in st and val > max_occurrence:
                    max_occurrence = val
                    max_key = key
                # print(max_key,max_occurrence)
            st.add(max_key)
            res.append(max_key)
            k -= 1
        return res
        