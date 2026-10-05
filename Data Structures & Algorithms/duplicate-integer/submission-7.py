class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmp = {}
        for num in nums:
            if num in hmp:
                return True
            hmp[num] = 1
        return False


