class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k %n
        
        for i, el in enumerate(nums[::-1][:k][::-1] + nums[::-1][k:][::-1]):
            nums[i] = el
    
nums = [1,2,3,4,5,6,7]
Solution().rotate(nums, 3)
print(nums)