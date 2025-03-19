class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        low = 0
        high = n - 1
        while low < high:
            mid = (low+high)//2
            if nums[mid] > target:
                high = mid + 1

            else:
                low = mid
        return mid
    
print(Solution().searchInsert([1,3,5,6], 5))
# print(Solution().searchInsert([1,3,5,6], 2))
# print(Solution().searchInsert([1,3,5,6], 7))
            