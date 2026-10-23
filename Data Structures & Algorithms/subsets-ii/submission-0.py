class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        def solve(idx, valid_subset):
            if idx >= n:
                if valid_subset not in res:
                    res.append(list(valid_subset))
                return
            valid_subset.append(nums[idx])
            solve(idx+1, valid_subset)
            valid_subset.pop()
            solve(idx+1, valid_subset)
        solve(0,[])
        return res