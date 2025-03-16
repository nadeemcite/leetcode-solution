import math
class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        low = 1
        n = len(ranks)
        high = ranks[0] * (cars**2)
        res = -1
        while low <= high:
            mid = (low + high) // 2
            total_cars = 0
            for rank in ranks:
                total_cars += int(math.sqrt(mid / rank))
            if total_cars >= cars:
                high = mid - 1
                res = mid
            else:
                low = mid + 1
        return res

print(Solution().repairCars([3,1,3,3,1,3], 42))