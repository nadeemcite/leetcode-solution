class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        op_count = 0
        for i in range(n-2):
            print(i, nums)
            if nums[i] == 0:
                nums[i], nums[i+1], nums[i+2] = 1 - nums[i], 1 - nums[i+1], 1 - nums[i+2]
                op_count += 1
            
        return op_count if sum(nums) == n else -1
            
        
print(Solution().minOperations([0,1,1,1,0,0]))