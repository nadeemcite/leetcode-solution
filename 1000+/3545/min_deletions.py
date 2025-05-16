from collections import Counter

class Solution(object):
    def minDeletion(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = Counter(s)
        
        if len(freq) <= k:
            return 0
        
        freqs = sorted(freq.values())
        
        deletions = 0
        
        remove_count = len(freq) - k
        
        for i in range(remove_count):
            deletions += freqs[i]
            
        return deletions
        

print(Solution().minDeletion("abc", 2))
print(Solution().minDeletion("aabb", 2))
print(Solution().minDeletion("yyyzz", 1))