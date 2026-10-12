class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []
        def solve(idx,total,temp):
            if total[0] == 0:
                res.append(list(temp))
                return
            if total[0] < 0 or len(candidates) <= idx:
                return
            total[0] -= candidates[idx]
            temp.append(candidates[idx])
            solve(idx+1,total,temp)
            temp.pop()
            total[0] += candidates[idx]
            while idx+1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            solve(idx+1,total,temp)
        solve(0,[target],[])
        return res