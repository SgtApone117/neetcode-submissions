class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        missing_number = 0
        for i in range(n+1):
            missing_number ^= i
        
        for num in nums:
            missing_number ^= num
        return missing_number