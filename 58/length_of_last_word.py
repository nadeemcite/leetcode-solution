class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])
        

if __name__ == "__main__":
    ptr = Solution()
    val = "hello my dear"
    print(ptr.lengthOfLastWord(val))