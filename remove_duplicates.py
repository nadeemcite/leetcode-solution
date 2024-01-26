class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j+=1
                nums[j] = nums[i]
        return j+1
        
nums = [0,0,1,1,2,2]
print(Solution().removeDuplicates(nums))
print(nums)