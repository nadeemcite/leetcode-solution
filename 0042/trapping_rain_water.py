class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 0:
            return 0
        max_left = [height[0]] * n
        max_right = [height[n-1]] * n
        total_area = 0
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])
        for i in range(n-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i])
        for i in range(1, n-1):
            area = min(max_left[i], max_right[i]) - height[i]
            if area >= 1:
                total_area += area
        return total_area



print(Solution().trap([4,2,0,3,2,5]))