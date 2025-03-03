class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        minima = prices[0]
        n = len(prices)
        for i in range(1, n):
            minima = min(prices[i], minima)
            profit = prices[i] - minima
            max_profit = max(profit, max_profit)
        return max_profit

        
        

print(Solution().maxProfit([7,3,6,1,5,4]))