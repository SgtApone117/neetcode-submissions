class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def solve(idx, valid_subset):
            if idx >= n:
                res.append(list(valid_subset))
                return
            valid_subset.append(nums[idx])
            solve(idx+1, valid_subset)
            valid_subset.pop()
            solve(idx+1,valid_subset)
        solve(0,[])
        return res
        