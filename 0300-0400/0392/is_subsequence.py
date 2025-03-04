class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) < 1:
            return False
        s_index = 0
        for l in t:
            if s[s_index] == l:
                s_index += 1   
            if s_index == len(s):
                break
        return s_index == len(s)
        
if __name__ == "__main__":
    ptr = Solution()
    s = ""
    t = "ahbgdc"
    print(ptr.isSubsequence(s,t))