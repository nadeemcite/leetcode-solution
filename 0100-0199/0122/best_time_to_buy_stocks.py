class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        i = 0
        total_profit = 0
        minima = prices[0]
        while i < n-1:
            print("i", i, "minima", minima)
            if prices[i] < prices[i-1] or minima > prices[i]:
                j = i+1
                minima = prices[i]

                while j<n-1 and minima < prices[j]:
                    j+=1
            if prices[i] > prices[i+1]:
                j = i+1
                maxima = prices[i]
                while j< n-1 and maxima > prices[j]:
                    j+=1
                if minima:
                    profit = maxima - minima
                    total_profit += profit
                    minima = None

            
            i+=1

        if minima is not None:
            total_profit += prices[n-1] - minima
        return total_profit
        


print(Solution().maxProfit([2,1,2,0,1]))