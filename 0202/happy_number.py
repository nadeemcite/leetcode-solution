cache = []
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num_sum = sum([
            int(n)*int(n) for n in list(str(n))
        ])
        print(n, num_sum)
        if num_sum == 1:
            return True
        elif n == num_sum or num_sum ==0:
            return False
        else:
            if num_sum in cache:
                return False
            else:
                cache.append(num_sum)
                return self.isHappy(num_sum)



if __name__ == "__main__":
    ptr = Solution()
    print(ptr.isHappy(13))