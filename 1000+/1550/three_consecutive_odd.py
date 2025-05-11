class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        cnt = 0
        for num in arr:
            if num%2 != 0:
                if cnt == 0:
                    cnt = 1
                else:
                    cnt+=1
            else:
                cnt = 0
            if cnt == 3:
                return True
        return False



print(Solution().threeConsecutiveOdds([1,1,1]))
# print(Solution().threeConsecutiveOdds([2,6,4,1]))
# print(Solution().threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))