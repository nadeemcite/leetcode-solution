class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = 9223372036854775807
        profit=0
        max_profit=0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price=prices[i]
            profit = prices[i] - min_price
            if profit>max_profit:
                max_profit=profit
        return max_profit
    

print(Solution().maxProfit([7,3,6,1,5,4]))
# print(Solution().maxProfit([7,6,4,3,1]))