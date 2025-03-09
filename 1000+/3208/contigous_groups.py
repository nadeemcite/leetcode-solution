class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        n = len(colors)
        count = 0
        left = 0

        for right in range(n + k - 1):
            if right > 0 and colors[right % n] == colors[(right - 1) % n]:
                left = right  
            
            if right - left + 1 >= k:
                count += 1  
        
        return count


print(Solution().numberOfAlternatingGroups([1,1,0,1], 4))