class Solution(object):
    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        patterns = []
        def dfs(pos, pattern):
            if pos == m:
                patterns.append(tuple(pattern))
                return
            for color in range(3):
                if pos > 0 and pattern[-1] == color:
                    continue
                pattern.append(color)
                dfs(pos + 1, pattern)
                pattern.pop()
        
        dfs(0, [])
        
        P = len(patterns)
        compatible = [[] for _ in range(P)]
        for i, p in enumerate(patterns):
            for j, q in enumerate(patterns):
                for r in range(m):
                    if p[r] == q[r]:
                        break
                else:
                    compatible[i].append(j)
        
        dp = [1] * P
        for _ in range(1, n):
            new_dp = [0] * P
            for j in range(P):
                total = 0
                for i in compatible[j]:
                    total += dp[i]
                new_dp[j] = total % MOD
            dp = new_dp
        
        return sum(dp) % MOD
    

print(Solution().colorTheGrid(1,1))
print(Solution().colorTheGrid(1,2))
print(Solution().colorTheGrid(5,5))
