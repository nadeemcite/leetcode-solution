class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        char_set = set()
        l = 0
        res = 0
        for r in range(n):
            while s[r] in char_set:
                char_set.remove(s[l])
                l+=1
            char_set.add(s[r])
            res = max(res, r - l +1)
        return res


print(Solution().lengthOfLongestSubstring("abcabcbb"))