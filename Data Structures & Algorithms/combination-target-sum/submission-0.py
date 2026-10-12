class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def solve(idx,total, temp):
            #print(total[0])
            if total[0] < 0 or len(nums) <= idx:
                return
            if total[0] == 0:
                res.append(list(temp))
                return
            total[0] -= nums[idx]
            temp.append(nums[idx])
            solve(idx,total,temp)
            total[0] += nums[idx]
            temp.pop()
            solve(idx+1,total,temp)
        solve(0,[target],[])
        #print(res)
        return res
