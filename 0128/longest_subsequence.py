class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        numset = set(nums)
        longest_streak = 0
        for num in numset:
            
            if num-1 not in numset:
                current_streak = 1
                current_num = num
                while current_num + 1 in numset:
                    current_streak += 1
                    current_num += 1
                if current_streak>longest_streak:
                    longest_streak = current_streak

        return longest_streak
    
print(Solution().longestConsecutive([2,20,4,10,3,4,5]))