class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)

        for i in range(n):
            # profit = 0
            for j in range(i,n):
                if i == j:
                    continue
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
                # print(max_profit)
        return max_profit
            
