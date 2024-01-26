import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        main_str = re.sub(r'[^a-zA-Z]', '', s).lower()
        return main_str == main_str[::-1]
        
if __name__ == "__main__":
    s = Solution()
    val = "A man, a plan, a canal: Panama"
    print(s.isPalindrome(val))