from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmp = defaultdict(int)
        n = len(nums)
        for i in range(n):
            rem = target-nums[i]
            if rem in hmp:
                return [hmp[rem], i]
            hmp[nums[i]] = i
        return [-1,-1]
        