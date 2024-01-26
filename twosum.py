class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i in range(len(nums)):
            v = target - nums[i]
            if v in map:
                return [map[v], i]
            map[nums[i]] = i
        return []
     
print(Solution().twoSum([3,2,4], 6))