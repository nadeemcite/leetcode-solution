class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        if n<3:
            return 0
        left_max = [height[0]] * n
        right_max = [height[n-1]] * n
        for i in range(1, n):
            left_max[i] = max(height[i],left_max[i-1] )
        for i in range(n-2, -1, -1):
            right_max[i] = max(height[i],right_max[i+1] )
        total_water = 0
        for i in range(1, n-1):
            val = min(left_max[i], right_max[i]) - height[i]
            if val > 0:
                total_water += val

        return total_water
    

print(Solution().trap([0,2,0,3,1,0,1,3,2,1]))