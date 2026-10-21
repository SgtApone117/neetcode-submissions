class Solution:
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1] * (n + 1)
        def solve(i):
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = cost[i] + min(solve(i+1), solve(i + 2))
            return memo[i]
        return min(solve(0),solve(1))