class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = dict()
        for i in range(len(nums)):
            if nums[i] in map:
                return True
            map[nums[i]] = i
        return False