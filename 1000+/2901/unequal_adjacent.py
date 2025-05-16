class Solution(object):
    def getWordsInLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        n = len(words)
        # dp[i]: max length of valid subseq ending at i
        dp = [1] * n
        # prev[i]: previous index in that subsequence, or -1
        prev = [-1] * n
        
        best_idx = 0  # index where dp is maximum
        
        for i in range(n):
            for j in range(i):
                # only consider j->i if groups differ and lengths match
                if groups[j] != groups[i] and len(words[j]) == len(words[i]):
                    # compute Hamming distance in O(m)
                    diff = 0
                    for c1, c2 in zip(words[j], words[i]):
                        if c1 != c2:
                            diff += 1
                            if diff > 1:
                                break
                    if diff == 1:
                        # we can extend the subsequence ending at j
                        if dp[j] + 1 > dp[i]:
                            dp[i] = dp[j] + 1
                            prev[i] = j
            # track where the overall best ends
            if dp[i] > dp[best_idx]:
                best_idx = i
        
        res = []
        cur = best_idx
        while cur != -1:
            res.append(words[cur])
            cur = prev[cur]
        res.reverse()
        return res

print(Solution().getWordsInLongestSubsequence(["bab","dab","cab"], [1,2,2]))
print(Solution().getWordsInLongestSubsequence(["a","b","c","d"], [1,2,3,4]))
