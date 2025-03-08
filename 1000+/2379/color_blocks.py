class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        n = len(blocks)
        min_r = k
        for i in range(n-k+1):
            cnt_w = 0
            for j in range(i, i+k):
                if blocks[j] == "W":
                    
                    cnt_w+=1
            if min_r > cnt_w:
                min_r = cnt_w
        return min_r

print(Solution().minimumRecolors("WBBWWBBWBW", 7))