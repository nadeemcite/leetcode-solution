class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        l = 0
        r = n - 1
        max_area = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(area, max_area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_area 


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))