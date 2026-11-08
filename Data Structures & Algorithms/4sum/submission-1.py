class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                start = j+1
                end = n-1
                while start < end:
                    total = nums[i]+nums[j]+nums[start]+nums[end]
                    if total == target:
                        temp = [nums[i],nums[j],nums[start],nums[end]]
                        res.append(temp)
                        start += 1
                        end -= 1
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
                    elif total > target:
                        end -= 1
                    else:
                        start += 1
        return res