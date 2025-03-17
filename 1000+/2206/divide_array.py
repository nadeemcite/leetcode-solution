class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        singles = set()
        for num in nums:
            if num in singles:
                singles.remove(num)
            else:
                singles.add(num)
        return len(singles) == 0

        

print(Solution().divideArray([3,2,3,2,2,2]))
print(Solution().divideArray([1,2,3,4]))