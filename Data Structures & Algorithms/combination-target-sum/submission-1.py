class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        def solve(idx,remaining_sum,valid_path):
            if remaining_sum[0] == 0:
                res.append(list(valid_path))
                return
            if idx >= n or remaining_sum[0] < 0:
                return
            valid_path.append(nums[idx])
            remaining_sum[0] -= nums[idx]
            solve(idx,remaining_sum,valid_path)
            if valid_path:
                remaining_sum[0] += valid_path.pop()
            solve(idx+1, remaining_sum,valid_path)
        solve(0,[target],[])
        return res