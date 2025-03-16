class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n<0:
            n *= -1
            x = 1.0/x
        sum = 1
        while n:
            if n%2 == 1:
                sum*=x
            x*=x
            n//=2
        return sum

if __name__ == "__main__":
    ptr = Solution()
    print(ptr.myPow(8,-2))