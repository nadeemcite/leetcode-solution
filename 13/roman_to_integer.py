class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        final_int = 0
        len_string = len(s)
        for i in range(len_string):
            if i<len_string-1 and symbol_to_int[s[i+1]]>symbol_to_int[s[i]]:
                final_int-=symbol_to_int[s[i]]
            else:
                final_int+=symbol_to_int[s[i]]

        return final_int
        
if __name__ == "__main__":
    ptr = Solution()
    val = "IV"
    print(ptr.romanToInt(val))