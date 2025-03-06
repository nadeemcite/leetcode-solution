class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        i = 0
        n = len(grid)
        final_sum = 0
        required_sum = ((n**2)*(n**2+1))/2
        num_passed = set()
        repeating_num = None
        while i<n:
            j=0
            while j<n:
                if grid[i][j] in num_passed:
                    repeating_num = grid[i][j]
                else:
                    final_sum += grid[i][j]
                    num_passed.add(grid[i][j])
                j+=1
            i+=1
        return [repeating_num, int(required_sum - final_sum)]



print(Solution().findMissingAndRepeatedValues([[1,3],[2,2]]))
print(Solution().findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))