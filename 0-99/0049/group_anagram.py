class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mem = {}
        for st in strs:
            alpha_ints = [0]*26
            for ch in st:
                ch_index = ord(ch) - ord('a')
                alpha_ints[ch_index] += 1
            alpha_str = str(alpha_ints)
            if alpha_str in mem:
                mem[alpha_str].extend([st])
            else:
                mem[alpha_str] = [st]
        return mem.values()
    
strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution().groupAnagrams(strs))