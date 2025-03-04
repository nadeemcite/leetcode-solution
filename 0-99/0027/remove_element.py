class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for i in range(len(nums)):
            if val != nums[i]:
                nums[j] = nums[i]
                j+=1
        return j

        
if __name__ == "__main__":
    ptr = Solution()
    nums = [1,2,3,1,2,3]
    val = ptr.removeElement(nums, 2)
    print(nums)
    print(val)