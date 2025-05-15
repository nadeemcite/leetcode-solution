class Solution(object):
    def getLongestSubsequence(self, words, groups):
        """
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        n = len(words)
        max_seq = []
        
        for start in range(n):
            temp_seq = [words[start]]
            last_group = groups[start]
            
            for i in range(start + 1, n):
                if groups[i] != last_group:
                    temp_seq.append(words[i])
                    last_group = groups[i]
            
            if len(temp_seq) > len(max_seq):
                max_seq = temp_seq
        
        return max_seq
    
print(Solution().getLongestSubsequence(["e","a","b"], [0,0,1]))
print(Solution().getLongestSubsequence(["a","b","c","d"], [1,0,1,1]))
