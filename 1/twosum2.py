class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mem = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in mem:
                return [mem[comp], i]
            mem[num] = i
        return []
