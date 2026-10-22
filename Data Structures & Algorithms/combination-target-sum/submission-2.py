class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        def solve(idx,remaining_sum,valid_path):
            if remaining_sum == 0:
                res.append(list(valid_path))
                return
            if idx >= n or remaining_sum < 0:
                return
            valid_path.append(nums[idx])
            solve(idx,remaining_sum-nums[idx],valid_path)
            valid_path.pop()
            solve(idx+1, remaining_sum,valid_path)
        solve(0,target,[])
        return res