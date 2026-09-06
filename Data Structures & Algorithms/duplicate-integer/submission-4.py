class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        n = len(sorted_nums)

        for i in range(n-1):
            if sorted_nums[i] == sorted_nums[i+1]:
                return True
        return False


