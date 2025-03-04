class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        f_arr = []
        z_arr = []
        i = 0
        while i<n-1:
            if nums[i] == nums[i+1]:
                if nums[i] == 0:
                    z_arr.append(0)
                else:
                    f_arr.append(nums[i] * 2)
                nums[i+1] = 0
            else:
                if nums[i] == 0:
                    z_arr.append(0)
                else:
                    f_arr.append(nums[i])
            i+=1
        return f_arr + [nums[n-1]] +  z_arr
    
print(Solution().applyOperations([1,2,2,1,1,0]))

        