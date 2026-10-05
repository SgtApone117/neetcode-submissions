class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        start = 0
        end = n - 1
        while start < end:
            val = nums[start] + nums[end]
            if val == target:
                return [start+1, end+1]
            if val < target:
                start += 1
            else:
                end -= 1
        return [-1,-1]