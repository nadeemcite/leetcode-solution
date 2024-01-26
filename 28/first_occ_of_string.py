class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        splits = haystack.split(needle)
        if len(splits)>1:
            return len(splits[0])
        else:
            return -1
        

if __name__ == "__main__":
    ptr = Solution()
    haystack = "leetcode"
    needle = "leeto"
    print(ptr.strStr(haystack, needle))