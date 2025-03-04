class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        pack = [0]*26
        if len(s) != len(t):
            return False
        for i, l in enumerate(s):
            index_s = ord(l) - ord('a')
            index_t = ord(t[i]) - ord('a')
            pack[index_s] += 1
            pack[index_t] -= 1
        
        return all(count==0 for count in pack)

