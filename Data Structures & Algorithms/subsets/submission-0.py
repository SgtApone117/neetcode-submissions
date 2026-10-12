class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        def solve(nums,idx,temp):
            if idx >= len(nums):
                res.append(list(temp))
                return
            temp.append(nums[idx])
            solve(nums,idx + 1, temp)
            temp.pop()
            solve(nums,idx+1,temp)
            
        solve(nums,0,[])
        # print(res)
        return res
