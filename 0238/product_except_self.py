class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix_arr = [1] * n
        postfix_arr = [1] * n
        final_arr = []

        for i in range(n):
            if i>0:
                prefix_arr[i] = nums[i-1] if i==1 else prefix_arr[i-1] * nums[i-1]

            j = n - i - 1
            if j < n - 1:
                postfix_arr[j] = nums[j+1] if j == n-2 else postfix_arr[j+1] * nums[j+1]
            print(prefix_arr, postfix_arr)

        for i in range(n):
            final_arr.append(prefix_arr[i]*postfix_arr[i])
        return final_arr
    
print(Solution().productExceptSelf([1,2,3,4]))