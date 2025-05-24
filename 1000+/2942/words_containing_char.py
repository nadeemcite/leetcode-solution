class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        return [i for i, w in enumerate(words) if x in w]
    
print(Solution().findWordsContaining(["leet","code"], "e"))
print(Solution().findWordsContaining(["abc","bcd","aaaa","cbc"], "a"))
print(Solution().findWordsContaining(["abc","bcd","aaaa","cbc"], "z"))
