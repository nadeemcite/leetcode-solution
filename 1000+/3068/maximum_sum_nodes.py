class Solution(object):
    def maximumValueSum(self, nums, k, edges):
        """
        :type nums: List[int]
        :type k: int
        :type edges: List[List[int]]
        :rtype: int
        """
        base = sum(nums)
        
        deltas = [(num ^ k) - num for num in nums]
        
        pos = [d for d in deltas if d > 0]
        pos.sort()
        sum_pos = sum(pos)
        
        if len(pos) % 2 == 0:
            return base + sum_pos
        
        drop_gain = sum_pos - pos[0]
        
        nonpos = [d for d in deltas if d <= 0]
        if nonpos:
            add_gain = sum_pos + max(nonpos)
            best_gain = max(drop_gain, add_gain)
        else:
            best_gain = drop_gain
        
        return base + best_gain
    

print(Solution().maximumValueSum([1,2,1], 3, [[0,1],[0,2]]))
print(Solution().maximumValueSum([2,3], 7, [[0,1]]))
print(Solution().maximumValueSum([7,7,7,7,7,7], 3, [[0,1],[0,2],[0,3],[0,4],[0,5]]))
