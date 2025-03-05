class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        perimeter = 4 * (n -1)
        while n > 1:
            n-=1
            perimeter += 4*(n-1) or 1
        return perimeter
        

print(Solution().coloredCells(2))