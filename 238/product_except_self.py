class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k = len(nums)
        prefix_products = [1] * k
        postfix_products = [1] * k
        final_arr = []
        for i in range(len(nums)):
            if i > 0:
                prefix_products[i] = nums[i - 1] if i ==1 else nums[i - 1] * prefix_products[i - 1]
            j = k - i - 1
            if j < k - 1:
                postfix_products[j] = nums[j+1] if j == k-2 else postfix_products[j+1] *nums[j+1]
            
            
        for i in range(len(nums)):
            final_arr.append(prefix_products[i] * postfix_products[i])
        return final_arr
    
print(Solution().productExceptSelf([1,2,3,4]))