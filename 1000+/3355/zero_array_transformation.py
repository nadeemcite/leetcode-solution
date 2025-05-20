class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        diff = [0] * (n + 1)
        for l, r in queries:
            diff[l]   += 1
            diff[r+1] -= 1

        cover = [0] * n
        curr = 0
        for i in range(n):
            curr      += diff[i]
            cover[i]  = curr

        for i in range(n):
            if cover[i] < nums[i]:
                return False

        return True
    

print(Solution().isZeroArray([1,0,1], [[0,2]]))
print(Solution().isZeroArray([4,3,2,1], [[1,3],[0,2]]))