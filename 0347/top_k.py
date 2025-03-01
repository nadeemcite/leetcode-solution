import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count_map = {}
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 0
        queue = []
        for i, (num, count) in enumerate(count_map.items()):
            if i<k:
                heapq.heappush(queue, (count, num))
            else:
                heapq.heappushpop(queue, (count, num))

        return [el[1] for el in queue]
        
