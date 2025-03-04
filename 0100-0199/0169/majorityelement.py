class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        final_dict = {}
        for num in nums:
            if num in final_dict:
                final_dict[num]+=1
            else:
                final_dict[num]=1
        target=len(nums)//2
        for k, v in final_dict.items():
            if v > target:
                return k
        return 0

print(Solution().majorityElement([2,2,1,1,1,2,2]))