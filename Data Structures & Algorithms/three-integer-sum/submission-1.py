class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i + 1
            end = n-1
            while start < end:
                total = nums[i]+nums[start]+nums[end]
                if total == 0:
                    temp = [nums[i],nums[start],nums[end]]
                    res.append(temp)
                    start += 1
                    end -= 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                elif total > 0:
                    end -= 1
                else:
                    start += 1
        return res
                    
