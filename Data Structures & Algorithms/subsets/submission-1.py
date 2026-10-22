class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def solve(idx,subset):
            if idx >= len(nums):
                res.append(list(subset))
                return
            subset.append(nums[idx])
            solve(idx+1,subset)
            subset.pop()
            solve(idx+1,subset)
        solve(0,[])
        return res
