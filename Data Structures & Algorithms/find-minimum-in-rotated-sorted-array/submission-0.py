class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1
        ans = nums[high]
        while low <= high:
            mid = (low + high) // 2
            ans = min(ans, nums[mid])
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        return ans

