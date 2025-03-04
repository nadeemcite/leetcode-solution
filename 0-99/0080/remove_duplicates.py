class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n==0:
            return 0
        last_num = nums[0]
        i = 1
        occ = 1
        j = 1
        while i < n:
            if last_num == nums[i]:
                occ += 1
            else:
                last_num = nums[i]
                occ = 1
            if occ > 2:
                i += 1
                continue
            else:
                print(j)
                nums[j] = nums[i]
                j+=1
            i += 1
        return j, nums
    
print(Solution().removeDuplicates([0,0,1,1,1,1,2,3,3]))