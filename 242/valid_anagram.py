from collections import defaultdict


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
    
    def isAnagram2(self, s, t):
        c = defaultdict(int)
        for x in s:
            c[x] += 1
        for x in t:
            x[x] -= 1
        
        for v in c.values():
            if v!=0:
                return False
        return True

if __name__ == "__main__":
    ptr = Solution()
    s = "abba"
    t = "dog cat cat dog"
    print(ptr.isAnagram(s,t))