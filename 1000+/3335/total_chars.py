class Solution(object):
    def lengthAfterTransformations(self, s, t):
        """
        :type s: str
        :type t: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp_prev = [1] * 26
        for _ in range(t):
            dp_curr = [0] * 26
            for i in range(25):
                dp_curr[i] = dp_prev[i+1]
            dp_curr[25] = (dp_prev[0] + dp_prev[1]) % MOD
            dp_prev = dp_curr
        ans = 0
        base = ord('a')
        for ch in s:
            ans = (ans + dp_prev[ord(ch) - base]) % MOD

        return ans
    

print(Solution().lengthAfterTransformations("abcyy", 2))
print(Solution().lengthAfterTransformations("azbk", 1))