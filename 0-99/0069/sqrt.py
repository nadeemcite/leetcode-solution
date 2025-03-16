class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x
        while low<=high:
            mid = (low+high)//2
            if mid * mid > x:
                high = mid - 1
            elif mid * mid < x:
                low = mid + 1
            else:
                return mid
        return high
            
            
        

if __name__ == "__main__":
    ptr = Solution()
    print(ptr.mySqrt(8))