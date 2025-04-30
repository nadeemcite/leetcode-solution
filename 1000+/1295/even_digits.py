import math
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len([
            num for num in nums
            if int(math.log(num-1, 10)) % 2 != 0
        ])
    
print(Solution().findNumbers([12,345,2,6,7896]))