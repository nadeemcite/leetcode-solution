class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0]
        for word in strs[1:]:
            
            common_prefix = ""
            for i, l in enumerate(prefix):
                if i<len(word) and l == word[i]:
                    common_prefix+=l
                else:
                    break
            if common_prefix == "":
                return common_prefix
            prefix = common_prefix

        return prefix

if __name__ == "__main__":
    ptr = Solution()
    val = ["flower","flow","flight"]
    print(ptr.longestCommonPrefix(val))