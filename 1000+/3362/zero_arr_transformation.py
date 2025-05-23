import heapq

class Solution(object):
    def maxRemoval(self, nums, queries):
        n, m = len(nums), len(queries)
        starts = [[] for _ in range(n)]
        for l, r in queries:
            starts[l].append(r)

        heap = []
        diff = [0] * (n + 1)
        cur_dec = 0 
        used = 0 

        for i in range(n):
            for r in starts[i]:
                heapq.heappush(heap, -r)

            while heap and -heap[0] < i:
                heapq.heappop(heap)

            cur_dec += diff[i]
            need = nums[i] + cur_dec

            while need > 0:
                while heap and -heap[0] < i:
                    heapq.heappop(heap)
                if not heap:
                    return -1

                r = -heapq.heappop(heap)
                used += 1

                diff[i]    -= 1
                diff[r+1]  += 1
                cur_dec    -= 1
                need       -= 1

        return m - used
    

print(Solution().maxRemoval([2,0,2], [[0,2],[0,2],[1,1]]))
print(Solution().maxRemoval([1,1,1,1], [[1,3],[0,2],[1,3],[1,2]]))
print(Solution().maxRemoval([1,2,3,4], [[0,3]]))
print(Solution().maxRemoval([0,3], [[0,1],[0,0],[0,1],[0,1],[0,0]]))

print(Solution().maxRemoval([0,0,3], [[0,2],[1,1],[0,0],[0,0]]))

