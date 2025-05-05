class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [0] * (max(n + 1, 4))
        dp[0], dp[1], dp[2] = 1, 1, 2  # Base cases
        
        for i in range(3, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD
        
        return dp[n]