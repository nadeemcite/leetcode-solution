class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        return [
            nums[el] for el in nums
        ]
        
print(Solution().buildArray([0,2,1,5,3,4]))
print(Solution().buildArray([5,0,1,2,3,4]))