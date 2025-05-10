class Solution(object):
    def minSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        fixed_sum_1 = sum(nums1)
        fixed_sum_2 = sum(nums2)
        count_0_1 = sum([1 for el in nums1 if el == 0])
        count_0_2 = sum([1 for el in nums2 if el == 0])
        target_sum_1 = fixed_sum_1 + count_0_1
        target_sum_2 = fixed_sum_2 + count_0_2
        min_target = max(target_sum_1, target_sum_2)
        zeros_required_1 = min_target - fixed_sum_1
        if zeros_required_1 > 0 and count_0_1 == 0:
            return -1
        
        zeros_required_2 = min_target - fixed_sum_2
        if zeros_required_2 > 0 and count_0_2 == 0:
            return -1
        return min_target


print(Solution().minSum([3,2,0,1,0], [6,5,0]))
print(Solution().minSum([2,0,2,0], [1,4]))
print(Solution().minSum([0,17,20,17,5,0,14,19,7,8,16,18,6], [21,1,27,19,2,2,24,21,16,1,13,27,8,5,3,11,13,7,29,7]))