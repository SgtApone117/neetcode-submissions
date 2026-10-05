class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmp = {}
        for i in range(len(nums)):
            res = target-nums[i]
            if res in hmp:
                return [hmp[res],i]
            hmp[nums[i]] = i
        return [-1,-1]
        