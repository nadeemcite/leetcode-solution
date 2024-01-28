class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        key_dict = {}
        val_dict = {}
        for i, letter in enumerate(s):
            if letter in key_dict:
                if key_dict[letter] != t[i]:
                    return False
            else:
                if t[i] in val_dict:
                    return False
                key_dict[letter] = t[i]
                val_dict[t[i]] = letter
        return True

        

if __name__ == "__main__":
    ptr = Solution()
    s = "badc"
    t = "baba"
    print(ptr.isIsomorphic(s,t))