class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        low = 1
        high = n - 1

        while low < high:
            mid = (high+low)//2

            count = 0
            for num in nums:
                if num <= mid:
                    count += 1

            if count > mid:
                high = mid
            else:
                low = mid + 1
        return low    