class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l, r]
            elif numbers[l] + numbers[r] > target:
                r = r - 1
            else:
                l = l +1
        return []
    

print(Solution().twoSum([-1,0], -1))