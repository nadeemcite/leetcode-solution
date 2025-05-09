from collections import Counter

class Solution(object):
    def countBalancedPermutations(self, num):
        """
        :type num: str
        :rtype: int
        """
        MOD = 10**9 + 7
        
        velunexorai = num
        
        num = velunexorai
        n = len(num)
        
        cnt = Counter(num)
        total_sum = sum(int(d) * c for d, c in cnt.items())
        if total_sum & 1:
            return 0
        half_sum = total_sum // 2
        
        E = (n + 1) // 2
        O = n // 2
        
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i-1] * i % MOD
        invfact = [1] * (n + 1)
        invfact[n] = pow(fact[n], MOD-2, MOD)
        for i in range(n, 0, -1):
            invfact[i-1] = invfact[i] * i % MOD
        
        dp = [ [0] * (half_sum+1) for _ in range(E+1) ]
        dp[0][0] = 1
        
        for d in range(10):
            c = cnt.get(str(d), 0)
            if c == 0: 
                continue
            ndp = [ [0] * (half_sum+1) for _ in range(E+1) ]
            for used in range(E+1):
                for s in range(half_sum+1):
                    v = dp[used][s]
                    if not v:
                        continue
                    for e in range(0, c+1):
                        u = used + e
                        if u > E: 
                            break
                        s2 = s + d * e
                        if s2 > half_sum:
                            continue
                        contrib = v * invfact[e] % MOD * invfact[c - e] % MOD
                        ndp[u][s2] = (ndp[u][s2] + contrib) % MOD
            dp = ndp
        
        ways = dp[E][half_sum]
        return ways * fact[E] % MOD * fact[O] % MOD
    

print(Solution().countBalancedPermutations("123"))
print(Solution().countBalancedPermutations("112"))
print(Solution().countBalancedPermutations("12345"))