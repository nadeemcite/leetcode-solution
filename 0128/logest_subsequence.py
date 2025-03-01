class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        sorted_nums = sorted(nums)
        print(sorted_nums)
        max_seq = 1
        current_seq = 1
        for i, num in enumerate(sorted_nums[:-1]):
            print(i, num, sorted_nums[i+1], current_seq)
            if num + 1 == sorted_nums[i+1]:
                current_seq+=1
            elif num == sorted_nums[i+1]:
                continue
            else:

                current_seq = 1
            if current_seq>max_seq:
                max_seq = current_seq
        return max_seq




print(Solution().longestConsecutive([1,0,1,2]))